import os


def get_tim_url() -> str:
    default_tim_url = 'http://localhost:8000'
    return os.getenv('TIM_URL', default_tim_url)
