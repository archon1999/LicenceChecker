import os

from django.db import models


def program_version_directory_path(instance, filename):
    program_version = instance.version
    return os.path.join('program_versions', program_version + '.exe')


class ProgramVersion(models.Model):
    programs = models.Manager()
    version = models.CharField(max_length=255)
    exe = models.FileField(upload_to=program_version_directory_path)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.version


class ValidAccount(models.Model):
    accounts = models.Manager()
    mac_address = models.CharField(max_length=255)
    host_name = models.CharField(max_length=255)
    program_version = models.ForeignKey(ProgramVersion,
                                        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.host_name
