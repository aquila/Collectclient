from distutils.core import setup
f=open("README.rst")
setup(name='Collectclient', version='0.01',
            py_modules=['collectclient'],
            requires=['pyzmq'],                  
            url="https://github.com/FFM/Collectorclient",
            author="Michael Bauer",
            author_email="mihi@lo-res.org",
            description="A client for the Network statistics Collector",
            long_description="\n".join(f)
                  )
