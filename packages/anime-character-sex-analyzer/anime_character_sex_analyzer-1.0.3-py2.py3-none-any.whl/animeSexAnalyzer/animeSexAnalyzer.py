from typing import Dict, Tuple
from imgutils.data import ImageTyping
from imgutils.generic import classify_predict_score, classify_predict

_REPO_ID = 'deepghs/anime_ch_sex'
_DEFAULT_MODEL_NAME = 'caformer_s36_v1.1_noconfuse'

def sex_rating_score(image: ImageTyping, model_name: str = _DEFAULT_MODEL_NAME) -> Dict[str, float]:
    return classify_predict_score(image, _REPO_ID, _DEFAULT_MODEL_NAME)


def sex_rating(image: ImageTyping, model_name: str = _DEFAULT_MODEL_NAME) -> Tuple[str, float]:
    return classify_predict(image, _REPO_ID, _DEFAULT_MODEL_NAME)
