import setuptools

#from setuptools import setup, find_packages
  
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = 'Test du tuto package'
  
setuptools.setup( 
        name ='monjeu', 
        version ='2.0.0', 
        author ='Josh', 
        author_email ='blablabla', 
        url ='blablabla2mongithub', 
        description ='blablabla3', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        packages = setuptools.find_packages(),
        #pour les entry points : dans les crochets [ nom_du_raccourci = le_chemin_du_script : main ]
        # il faut un "def main() :" dans le script à executer
        # pour un chemin type dossier1/script1.py
        # on va utiliser dossier1.script1:main
        entry_points ={ 
            'console_scripts': [ 
                'pendu = Pendu.script:main',
            ], 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        python_requires='>=3.6'
) 
