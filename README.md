#Citizen sourcing

##Utilisation de Pybossa

###Présentation générale de PyBossa

Sous pybossa, les ateliers se découpent en projets. Les projets correspondent à un "modèle de question" à poser. Chaque projet comporte des tâches. Une tâche décrit une question et les sources qui sont liées. 

Il est possible de générer des projets soit via l'interface web soit en ligne de commande.

####Utilisation de l'interface web

Dans l'onglet create, vous pouvez créer un projet PyBossa en spécifiant :
* le nom du projet
* le slug
* la description

Après la création du projet il sera possible par la suite de :
* modifier le template des questions
* d'importer des tâches
* d'exporter les tâches
* d'exporter les résultats (en csv ou en json)
* d'accéder aux statistiques

>Attention : au moment de la création du projet, ce dernier ne sera pas directement visible dans la partie projets. Si vous souhaitez vous assurer que le projet a bien été créé, vous pouvez vous rendre à l'adresse suivante : http://url-de-votre-serveur/project/nom_du_projet

####Utilisation de la ligne de commande

Il est également possible d'interagir avec l'application à travers un terminal.
Un tutoriel est proposé et montre les différentes commandes à utiliser : http://docs.pybossa.com/en/latest/user/pbs.html

Vous pourrez ainsi:

* ajouter un projet
* ajouter des tâches 
* supprimer des tâches
* mettre à jour les templates

####Utilisation de PBS

#####Installation

* Installation des composantes utiles :

```sh
sudo apt-get install pandoc
pip install pybossa-pbs
```
* Création du fichier de configuration
>Avant de passer à cette étape, vous devez créer un compte via l'interface web, vous rendre sur votre profil et copier votre clé d'API. Elle vous sera utile au moment de renseigner le fichier de configuration.

```sh
cd ~
vim .pybossa.cfg
```
vous devez compléter le fichier de la façon suivante :

```
[default]
server: http://theserver.com
apikey: yourkey
```

#####Commandes utiles

* Pour créer un projet : ```pbs create_project```
* Pour ajouter des tâches (à partir d'un fichier JSON) : ```pbs add_tasks --tasks-file your_file.json --tasks-type=json```
* Pour supprimer toutes les tâches : ```pbs delete_tasks```
* Pour mettre à jour un projet : ``pbs update_project ```

>Attention : À chaque modification d'un projet, ajout/suppression de tâches ou modification du template, vous devez exécuter la commande pbs update_project
 
###Liens utiles

Voici quelques liens utiles si vous souhaitez en savoir plus sur l'application :

* Installation de pybossa en local : http://pybossa.com/getting-started/

> Attention : la méthode utilisée pour installer l'application a changé et il se peut que vous rencontriez des problèmes. Dans ce cas-là, je vous conseille d'utiliser l'ancienne méthode d'installation.

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
* Configuration du projet : http://docs.pybossa.com/en/latest/user/project_settings.html
* En cas de problème, vous pouvez contacter la communauté de développeurs à cette adresse : info@pybossa.com

##Mode d'emploi pour Citizen sourcing

Citizen sourcing se décompose en deux projets, un premier où l'utilisateur devra choisir parmi plusieurs images et déterminer laquelle est la plus représentative d'une catastrophe et un second projet où la personne interrogée devra déterminer le statut de la zone prise en photo.

Chaque projet est décrit avec un fichier json qui est de la forme :

```json
{
    "name": "name of the project",
    "short_name": "slug of the project",
    "description": " a short description",
    "question": "a question"
}
```

1. Récupération des sources : clonez le dépôt :``` git clone https://github.com/quentinl-c/citizensourcing.git```
2. Ajout des sources dans le répertoire de l'application : copiez les répertoires de chaque projet dans le répertoire de pybossa
3. Ajout des informations sur les projets : pour chaque projet, éditez le fichier project.json pour renseigner le nom et la description que vous souhaitez lui donner. Faites de même avec long_description.md pour renseigner une description un peu plus important 
5. Ajout des projets à PyBossa : une fois que toutes les informations sur le projet sont renseignées, vous pouvez ajouter le projet (à faire pour les deux projets). Pour ce faire, vous devez vous rendre dans le répertoire du projet en question et faire la commande :```pbs create_project```  
6. Création des tâches : Pour chaque projet, les tâches sont décrites dans un fichier json qui se nomme tasks_file.json. À titre d'exemple, voici l'allure des fichiers json pour chaque projet :

Projet 1 :

Chaque élément du tableau correspond à une tâche, l'attribut len correspond au nombre de choix proposés, et img correspond à l'url de l'image à afficher.

Pour chaque tâche à ajouter, il faudra donc renseigner ces paramètres.

```json
[
	{"len":4,"img":"http://lorempixel.com/output/city-q-c-1330-480-6.jpg"},
	{"len":3,"img":"http://morsures.org/sites/morsures.org/files/lorem-ipsum-logo.jpg"},
	{"len":5,"img":"http://morsures.org/sites/morsures.org/files/lorem-ipsum-logo.jpg"}
]
``` 

Projet 2 :

La spécification des tâches pour le projet 2 est plus simple puisqu'il suffit juste de renseigner l'url des images que l'on souhaite afficher
```json
[
	{"img":"http://morsures.org/sites/morsures.org/files/lorem-ipsum-logo.jpg"},
	{"img":"http://dahoo.fr/wordpress/wp-content/uploads/2014/11/Lorem-Ipsum.jpg"}
]
```

Une fois les différentes informations renseignées, vous pouvez ajouter les tâches (il faudra faire ça pour chaque projet), pour ce faire, utilisez la commande :

```sh
pbs add_tasks --tasks-file tasks_file.json --tasks-type=json
```

* Récupération des résultats : vous pouvez télécharger les résultats de l'application en allant sur la page du projet puis dans Tasks et dans Export Task. Il vous suffira de cliquer sur Tasks Runs pour télécharger les résultats.