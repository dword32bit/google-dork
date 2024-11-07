import setuptools

setuptools.setup(
    name='google_dork',
    version='1.0',
    packages=['google_dork'],
    author='dword32bit',
    author_email='introboy333@gmail.com',
    description='Google Dorking CLI Tool without API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dword32bit/google-dork',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
)