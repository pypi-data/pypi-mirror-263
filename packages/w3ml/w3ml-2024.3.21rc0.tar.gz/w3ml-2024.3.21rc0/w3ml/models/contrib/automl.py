import os
from pathlib import Path
from typing import Dict, List

import pandas as pd
from autogluon.tabular import TabularPredictor

MODEL_DIR = Path.home().joinpath("models")


class AutoBinaryML:
    def __init__(
        self,
        model_name: str,
        model_version: str,
        train_data: pd.DataFrame,
        label: str,
        non_training_features: List[str] = [],
        eval_metric: str = "roc_auc",
        time_limit: int = None,
        excluded_model_types: List[str] = [
            "FASTTEXT",
            "AG_TEXT_NN",
            "TRANSF",
            "custom",
        ],
    ):
        """
        2024.03.21 v1 개발
        Contact : 이규남(kyunam@sk.com)

        AutoML을 통해 모델을 학습합니다.

        ## 참고 사항
        - AutoML이 자동으로 학습합니다.
        - 성능 지표를 설정할 수 있으나, 분류 문제의 경우 기본값인 `roc_auc` 사용을 권장합니다.
        - 회귀 문제에 분류 성능 지표를 세팅하거나 분류 문제에 회귀 성능 지표를 세팅하면 에러가 발생합니다.
        ## Args
        - model_name: (str) 모델명
        - model_name: (str) 모델버전
        - train_data: (`pandas.DataFrame`) 학습에 사용할 데이터 프레임
        - label: (str) train_data 내 라벨 컬럼 이름
        - non_training_features: (optional) (str) 학습에서 제외할 피쳐 이름 리스트. 후처리 전용 피쳐 등을 명세할 때 사용 가능 (기본값: [])
        - eval_metric: (optional) (str) 성능 지표 (기본값: `roc_auc`)
            - 분류 모델 가능한 값: `accuracy`|`balanced_accuracy`|`f1`|`f1_macro`|`f1_micro`|`f1_weighted`|`roc_auc`|`average_precision`|`precision`|`precision_macro`|`precision_micro`|`precision_weighted`|`recall`|`recall_macro`|`recall_micro`|`recall_weighted`|`log_loss`|`pac_score`
        - time_limit: (optional) (int) 학습 시간 제한 시간 (단위: 초). n개의 모델을 학습하는 경우 1/n초씩 사용. None인 경우 무제한 (기본값: None)
        - excluded_model_types: (optional) (List[str]) Banned subset of model types to avoid training during fit(), even if present in hyperparameters. Reference hyperparameters documentation for what models correspond to each value.
        ## Example
        # 학습 및 테스트 데이터 준비
        train_data, test_data = train_test_split(df, test_size=0.2, random_state=0)
        # 학습
        my_model_v1 = AutoBinaryML(
            train_data=train_data,
            label="some_label"
        )
        my_model_v1.fit()
        # 성능 확인
        print(my_model_v1.evaluate(test_data))
        print(my_model_v1.get_feature_importance(test_data))
        # predict 테스트
        print(my_model_v1.batch_prediction(test_data, "predict"))
        """
        assert isinstance(
            train_data, pd.DataFrame
        ), "`train_data은(는) pd.DataFrame 타입이어야 합니다.`"
        assert isinstance(label, str), "`label(는) str 타입이어야 합니다.`"
        assert isinstance(
            non_training_features, list
        ), "`non_training_features은(는) list 타입이어야 합니다.`"
        assert isinstance(time_limit, int), "`time_limit(는) int 타입이어야 합니다.`"
        assert isinstance(
            excluded_model_types, list
        ), "`excluded_model_types은(는) list 타입이어야 합니다.`"

        self.train_data = train_data
        self.label = label
        self.non_training_features = non_training_features
        self.eval_metric = eval_metric
        self.time_limit = time_limit
        self.excluded_model_types = excluded_model_types

    def fit(self):
        self.models = self._fit()
        os.rmdir(MODEL_DIR.joinpath(self.model_name, self.model_version))

    def _fit(self):
        columns = [
            f for f in self.train_data.columns if f not in self.non_training_features
        ] + [self.label]
        predictor = TabularPredictor(
            label=self.label,
            eval_metric=self.eval_metric,
            path=MODEL_DIR.joinpath(self.model_name, self.model_version),
            sample_weight="balance_weight",
            verbosity=0,
        )
        return predictor.fit(
            train_data=train_data[columns],
            presets="best_quality",
            time_limit=self.time_limit,
            excluded_model_types=self.excluded_model_types,
            keep_only_best=True,
        )

    def batch_prediction(self, batch_data: pd.DataFrame, predict_fn) -> pd.DataFrame:
        """
        AutoGluon을 통해 학습한 모델의 배치 예측을 지원합니다.
        """
        assert predict_fn in [
            "predict",
            "predict_proba",
        ], "배치 예측 시 `predict_fn`은 predict, predict_proba 중 하나의 값이어야 합니다."

        if predict_fn == "predict":
            return self.models.predict(batch_data)
        elif predict_fn == "predict_proba":
            return self.models.predict_proba(batch_data)

    def evaluate(self, test_data: pd.DataFrame) -> Dict[str, float]:
        """
        AutoGluon을 통해 학습한 모델의 성능을 계산합니다.
        ## 참고 사항
        - `fit` 함수를 통해 학습이 된 경우에만 정상적으로 동작합니다.
        - `fit` 함수에서는 모델 학습 후 한 차례 본 함수를 실행하여 `self.performance`에 저장합니다.
        ## Args
        - test_data: (optional) (`pandas.DataFrame`) 모델 성능 측정을 위한 테스트 데이터 프레임 (기본값: None)
        ## Example
        # 학습 및 테스트 데이터 준비
        train_data, test_data = train_test_split(df, test_size=0.2, random_state=0)
        # 학습
        my_model_v1.fit(
            train_data=train_data,
            test_data=test_data,
            label="some_label"
        )
        # 성능 계산
        print(my_model_v1.evaluate(test_data))
        """
        columns = [f for f in self.features if f not in self.non_training_features] + [
            self.label
        ]
        return self.models.evaluate(test_data[columns], silent=True)

    def get_feature_importance(self, test_data: pd.DataFrame) -> pd.Series:
        """
        AutoGluon을 통해 학습한 모델의 피쳐 중요도를 계산하여 `pandas.Series` 형식으로 리턴합니다.
        ## 참고 사항
        - `fit` 함수를 통해 학습이 된 경우에만 정상적으로 동작합니다.
        - `fit` 함수에서는 모델 학습 후 한 차례 본 함수를 실행하여 `self.feature_importance`에 저장합니다.
        ## Args
        - test_data: (optional) (`pandas.DataFrame`) 모델 성능 측정을 위한 테스트 데이터 프레임 (기본값: None)
        ## Example
        # 학습 및 테스트 데이터 준비
        train_data, test_data = train_test_split(df, test_size=0.2, random_state=0)
        # 학습
        my_model_v1.fit(
            train_data=train_data,
            test_data=test_data,
            label="some_label"
        )
        # 성능 계산
        print(my_model_v1.get_feature_importance(test_data))
        """
        columns = [f for f in self.features if f not in self.non_training_features] + [
            self.label
        ]
        return self.models.feature_importance(test_data[columns], silent=True)[
            "importance"
        ]
