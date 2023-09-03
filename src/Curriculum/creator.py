from account.models import User
from models import generator
from .models import Curriculum, CurriculumSyllabi, SyllabiTopic
from Resource.models import Resource
from Quiz.models import QOption, Quiz
from django.db import transaction


@transaction.atomic
def generate_curriculum(skill: str, experience: str, weekly_time: int, user: User):
    text = f"""
    Generate a curriculum for a developer who wants to learn
    {skill} with {experience} experience. The developer has
    {weekly_time} hours per week to study.
    """
    format = ''
    with open("format.json", "r") as f:
        format = f.read()
    if not format:
        raise Exception("Format not found")
    json_data = generator.generate_with_format(text, format)

    curriculum = Curriculum.objects.create(
        name=json_data['name'],
        description=json_data['description'],
        prerequisites=json_data['prerequisites'],
        objective=json_data['objective'],
        difficulty=json_data['difficulty'],
        private=True
    )

    for module in json_data['modules']:
        syllabi = CurriculumSyllabi.objects.create(
            curriculum=curriculum,
            title=module['title'],
            description=module['description']
        )

        for topic in module['topics']:
            syllabi_topic = SyllabiTopic.objects.create(
                syllabi=syllabi,
                title=topic['title'],
                description=topic['description']
            )

            for resource in topic['resources']:
                rtype = "O"
                if resource['type'] == 'course':
                    rtype = "C"
                elif resource['type'] == 'video':
                    rtype = "V"
                elif resource['type'] == 'article':
                    rtype = "A"
                elif resource['type'] == 'book':
                    rtype = "B"

                Resource.objects.create(
                    syllabi_topic=syllabi_topic,
                    title=resource['title'],
                    description=resource['description'],
                    url=resource['url'],
                    rtype=rtype,
                )

            for quiz in topic['quizzes']:
                quiz_model = Quiz.objects.create(
                    topic=syllabi_topic,
                    question=quiz['question']
                )

                for option in quiz['options']:
                    QOption.objects.create(
                        quiz=quiz_model,
                        option=option['option'],
                        reason=option['reason'],
                        is_correct=option['is_correct']
                    )

    user.enroll_curriculum(curriculum)
    return curriculum
