import setuptools

setuptools.setup(
    author = 'David Jacobs',
    author_email = 'david@29.io',
    description = 'A python library for interacting with the Apple Push Notification Service',
    download_url = 'https://github.com/djacobs/PyAPNs',
    license = 'unlicense.org',
    name = 'apns-ng',
    py_modules = ['apns'],
    scripts = ['apns-send'],
    url = 'http://29.io/',
    version = '2.1.0',
    classifiers = [ 'Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: Apache Software License',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3.5',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3.8',
                    'Topic :: Software Development :: Libraries',
                    'Topic :: Software Development :: Libraries :: Python Modules']
)
