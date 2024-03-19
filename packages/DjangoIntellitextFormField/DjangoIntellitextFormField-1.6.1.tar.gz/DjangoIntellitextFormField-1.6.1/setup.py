from setuptools import setup
import re
project_name = 'DjangoIntellitextFormField'


def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/_version.py').read())
    return result.group(1)


setup(
    name='DjangoIntellitextFormField',
    version=get_property('__version__', project_name), #'1.5',
    packages=['DjangoIntellitextFormField'],
    url='https://github.com/amcsparron2793-Water/DjangoIntellitextFormField',
    download_url=f'https://github.com/amcsparron2793-Water/DjangoIntellitextFormField/archive/refs/tags/{get_property("__version__", project_name)}.tar.gz',
    keywords=['Django', 'Intellitext', 'PickList'],
    license='MIT License',
    author='Amcsparron',
    author_email='amcsparron@albanyny.gov',
    description='adds intellitext forms and fields to a django project'
)
