import random
from datetime import datetime, timedelta
from typing import Callable


def nullable_factory[T](
    generator: Callable[[], T], probability_of_none: float = 0.3
) -> Callable[[], T | None]:
    return lambda: generator() if random.random() < probability_of_none else None


def generate_submission_time(start_time: datetime) -> str:
    delay = timedelta(hours=random.randint(1, 6))
    return (start_time + delay).strftime('%Y-%m-%d %H:%M:%S')


# def generate_open_answer_seeder(
#     num_records: int, open_question: List[OpenQuestion], attempts: List[Attempt]
# ) -> List[OpenAnswer]:
#     return [
#         OpenAnswer(
#             open_question_id=random.choice(open_question).id,
#             attempt_id=random.choice(attempts).id,
#         )
#         for _ in range(num_records)
#     ]
