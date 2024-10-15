from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_descendants(self):
        descendants = []

        def fetch_descendants(node, level):
            if level > 4:
                return
            children = node.children.all().select_related('parent')
            descendants.extend(children)
            list(map(lambda child: fetch_descendants(child, level + 1), children))

        fetch_descendants(self, 1)
        return descendants