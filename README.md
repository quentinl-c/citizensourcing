#Citizen sourcing

##Utilisation de Pybossa

###Présentation générale de PyBossa

Sous pybossa, les ateliers se découpent en projets. Les projets correspondent à un "modèle de question" à poser. Chaque projet comporte des tâches. Une tâche décrit une question et le sources qui sont liées. 

Il est possible de générer des procjets soit via l'interface web soit en ligne de commande.

####Utilisation de l'interface web

Dans l'onglet create, vous pouvez créer un projet PyBossa en spécifiant :
* le nom du projet
* le slug
* la description

Après la craétion du projet il sera possible par la suite de :
* modifier le template des questions
* d'importer des tâches
* d'exporter les tâches
* d'exporter les résultats (en csv ou en json)
* d'accèder aux statistiques

####Utilisation de la ligne de commande

Il est également possible d'interagir avec l'application à travers un terminal.
Un tutoriel est proposé et montre les différentes commandes à utiliser : http://docs.pybossa.com/en/latest/user/pbs.html

Vous pourrez ainsi:

* ajouter un projet
* ajouter des tâches 
* suprimmer des tâches
* mettre à jour les templates

###Liens utiles

Voici quelques liens utiles si vous souhaitez en savoir plus sur l'application :

* Installation de pybossa en local : http://pybossa.com/getting-started/

> Attention : la méthode utilisée pour installer l'application a changé et il se peut que vous rencontriez des problème. Dans ce cas là, je vous conseille d'utiliser l'ancienne méthode d'installation :

```sh
git clone https://github.com/PyBossa/pybossa
cd pybossa
vagrant plugin install vagrant-ansible-local
vagrant up

vagrant ssh
python run.py
```

* Création d'un projet : http://docs.pybossa.com/en/latest/user/tutorial.html
* Utilisation de la ligne de commande : http://docs.pybossa.com/en/latest/user/pbs.html
* Configuration du projet
* En cas de problème, vous pouvez contacter la communauté de développeurs à cette adresse : info@pybossa.com

##Mode d'emploi pour Citizen sourcing

Citizen sourcing se décompse en deux projets, un premier où l'utilisateur devra choisor parmi plusieurs images et déterminer laquelle est la plus représentative d'une catastrophe et un second projet où la personne intérrogée devra determiner le statu de la zone prise en photo.

Chaque projet est décrit avec un fichier json qui est de la forme :

```json
{
    "name": "name of the project",
    "short_name": "slug of the project",
    "description": " a short description",
    "question": "a question"
}
```


