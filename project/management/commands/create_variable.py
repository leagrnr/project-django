from django.core.management.base import BaseCommand
from project.models import Project

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        project1 = Project.objects.create(name='Project1')
        project2 = Project.objects.create(name='Project2')

        children_names1 = ['Child1', 'Child2', 'Child3', 'Child4']
        children1 = list(map(lambda name: Project.objects.create(name=name, parent=project1), children_names1))

        children_names2 = ['Child5', 'Child6', 'Child7', 'Child8']
        children2 = list(map(lambda name: Project.objects.create(name=name, parent=project2), children_names2))

        self.stdout.write(self.style.SUCCESS('Les variables ont été créées avec succès'))