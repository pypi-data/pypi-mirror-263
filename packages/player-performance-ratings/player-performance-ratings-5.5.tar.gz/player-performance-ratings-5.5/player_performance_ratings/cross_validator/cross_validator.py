import copy
import inspect
from typing import Optional

import pandas as pd
from player_performance_ratings import ColumnNames

from player_performance_ratings.scorer.score import BaseScorer
from player_performance_ratings.transformation.base_transformer import BaseTransformer, BasePostTransformer

from player_performance_ratings.cross_validator._base import CrossValidator
from player_performance_ratings.predictor._base import BasePredictor

class MatchCountCrossValidator(CrossValidator):

    def __init__(self,
                 match_id_column_name: str,
                 validation_match_count: int,
                 scorer: Optional[BaseScorer] = None,
                 n_splits: int = 3):
        super().__init__(scorer=scorer)
        self.n_splits = n_splits
        self.match_id_column_name = match_id_column_name
        self.validation_match_count = validation_match_count

    def generate_validation_df(self,
                               df: pd.DataFrame,
                               predictor: BasePredictor,
                               column_names: ColumnNames,
                               estimator_features: Optional[list[str]] = None,
                               post_transformers: Optional[list[BasePostTransformer]] = None,
                               return_features: bool = False,
                               add_train_prediction: bool = False
                               ) -> pd.DataFrame:

        predictor = copy.deepcopy(predictor)
        ori_cols = df.columns.tolist()

        validation_dfs = []
        df = df.assign(__cv_match_number=pd.factorize(df[self.match_id_column_name])[0])
        for post_transformer in post_transformers:
            post_transformer.reset()
            df = post_transformer.generate_historical(df, column_names=column_names)
        max_match_number = df['__cv_match_number'].max()
        train_cut_off_match_number = max_match_number - self.validation_match_count * self.n_splits + 1
        step_matches = self.validation_match_count

        train_df = df[(df['__cv_match_number'] < train_cut_off_match_number)]
        if len(train_df) < 0:
            raise ValueError(
                f"train_df is empty. train_cut_off_day_number: {train_cut_off_match_number}. Select a lower validation_match value.")
        validation_df = df[(df['__cv_match_number'] >= train_cut_off_match_number) & (
                df['__cv_match_number'] < train_cut_off_match_number + step_matches)]

        for idx in range(self.n_splits):

            predictor.train(train_df, estimator_features=estimator_features)

            if idx == 0 and add_train_prediction:
                train_df = train_df[[c for c in train_df.columns if c not in predictor.columns_added]]
                train_df = predictor.add_prediction(train_df)
                validation_dfs.append(train_df)

            validation_df = validation_df[[c for c in validation_df.columns if c not in predictor.columns_added]]
            validation_df = predictor.add_prediction(validation_df)
            validation_dfs.append(validation_df)

            train_cut_off_match_number = train_cut_off_match_number + step_matches
            train_df = df[(df['__cv_match_number'] < train_cut_off_match_number)]
            validation_df = df[(df['__cv_match_number'] >= train_cut_off_match_number) & (
                    df['__cv_match_number'] < train_cut_off_match_number + step_matches)]

        concat_validation_df = pd.concat(validation_dfs).drop(columns=['__cv_match_number'])
        if not return_features:
            concat_validation_df = concat_validation_df[ori_cols + predictor.columns_added]

        return concat_validation_df


class MatchKFoldCrossValidator(CrossValidator):
    def __init__(self,
                 match_id_column_name: str,
                 date_column_name: str,
                 scorer: Optional[BaseScorer] = None,
                 min_validation_date: Optional[str] = None,
                 n_splits: int = 3
                 ):
        super().__init__(scorer=scorer)
        self.match_id_column_name = match_id_column_name
        self.date_column_name = date_column_name
        self.n_splits = n_splits
        self.min_validation_date = min_validation_date

    def generate_validation_df(self,
                               df: pd.DataFrame,
                               predictor: BasePredictor,
                               column_names: ColumnNames,
                               estimator_features: Optional[list[str]] = None,
                               post_transformers: Optional[list[BasePostTransformer]] = None,
                               return_features: bool = False,
                               add_train_prediction: bool = False
                               ) -> pd.DataFrame:

        predictor = copy.deepcopy(predictor)
        validation_dfs = []
        ori_cols = df.columns.tolist()

        estimator_features = estimator_features or []
        post_transformers = post_transformers or []

        if not self.min_validation_date:
            unique_dates = df[self.date_column_name].unique()
            median_number = len(unique_dates) // 2
            self.min_validation_date = unique_dates[median_number]

        df = df.assign(__cv_match_number=range(len(df)))
        min_validation_match_number = df[df[self.date_column_name] >= self.min_validation_date][
            "__cv_match_number"].min()
        for post_transformer in post_transformers:
            post_transformer.reset()
            df = post_transformer.generate_historical(df, column_names=column_names)


        max_match_number = df['__cv_match_number'].max()
        train_cut_off_match_number = min_validation_match_number
        step_matches = (max_match_number - min_validation_match_number) / self.n_splits
        train_df = df[(df['__cv_match_number'] < train_cut_off_match_number)]
        if len(train_df) < 0:
            raise ValueError(
                f"train_df is empty. train_cut_off_day_number: {train_cut_off_match_number}. Select a lower validation_match value.")
        validation_df = df[(df['__cv_match_number'] >= train_cut_off_match_number) & (
                df['__cv_match_number'] < train_cut_off_match_number + step_matches)]

        for idx in range(self.n_splits):
            predictor.train(train_df, estimator_features=estimator_features)

            if idx == 0 and add_train_prediction:
                train_df = train_df[[c for c in train_df.columns if c not in predictor.columns_added]]
                train_df = predictor.add_prediction(train_df)
                validation_dfs.append(train_df)

            validation_df = validation_df[[c for c in validation_df.columns if c not in predictor.columns_added]]
            validation_df = predictor.add_prediction(validation_df)
            validation_dfs.append(validation_df)

            train_cut_off_match_number = train_cut_off_match_number + step_matches
            train_df = df[(df['__cv_match_number'] < train_cut_off_match_number)]

            if idx == self.n_splits - 2:
                validation_df = df[(df['__cv_match_number'] >= train_cut_off_match_number)]
            else:
                validation_df = df[(df['__cv_match_number'] >= train_cut_off_match_number) & (
                        df['__cv_match_number'] < train_cut_off_match_number + step_matches)]

        concat_validation_df = pd.concat(validation_dfs).drop(columns=['__cv_match_number'])
        if not return_features:
            concat_validation_df = concat_validation_df[ori_cols + predictor.columns_added]

        return concat_validation_df
