import random

from mongo_data_generating.models.models import *


def faculty_factory() -> Faculty:
    field_of_studies = []
    for _ in range(random.randint(1, 10)):
        terms = []
        for _ in range(random.randint(1, 10)):
            courses = [Course() for _ in range(random.randint(1, 7))]
            terms.append(Term(courses=courses))

        field_of_studies.append(FieldOfStudy(terms=terms))

    faculty_administrators = [
        FacultyAdministrator()
        for _ in range(random.randint(1, 3))
    ]
    faculty = Faculty(
        faculty_administrators=faculty_administrators,
        fields_of_study=field_of_studies
    )
    return faculty
