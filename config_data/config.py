from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: str
    channel: int
    support_id: int


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=env('ADMIN_IDS'),
                               channel=env('CHANNEL'),
                               support_id=env('SUPPORT_ID')))
