# Trabajo Práctico Final Foundations

## Ejercicio 1: Elección de dataset.

Crear un Pull Request con un archivo en formato **markdown** expliando el **dataset elegido** y una breve descripción de **al menos 4 preguntas de negocio** que se podrían responder teniendo esos datos en una base de datos relacional de manera que sean consultables con **lenguaje SQL**.

### _Respuesta 1:_
* El Dataset elegido es un dataset llamado **Amid_Deals.csv**, es un dataset obtenido de un curso de Datacamp y que además está en una competencia de Kaggle. Este dataset tiene 6 columnas: **id, product, client, status, amount, num_users**.
    * id [integer]: Es la Primary Key.
    * product [text]: Son los distintos tipos de productos que vende amid.
    * client [text]: Indica si son Clientes Corrientes o Clientes Nuevos.
    * status [text]: Indica si amid ganó o perdió dinero.
    * amount [DECIMAL(8,2)]: Muestra la cantidad de dinero que ganó amid.
    * num_users [integer]: Indica la cantidad de clientes que compraron un producto en una transacción.
* Las preguntas de negocio que se podrían responder con lenguaje SQL son:

 1. ¿Cuántos clientes habituales tiene? y ¿Cuántos clientes nuevos tiene?.
 2. ¿Cuáles son los productos más comercializados y que dejan mayores ganancias? y ¿Cuáles son los productos menos comercializados y que dejan menores ganancias?.
 3. ¿Qué producto tiene la mayor cantidad de clientes que lo adquieren? y ¿Qué producto tiene la menor cantidad de clientes que lo adquieren?.
 4. ¿Con qué productos amid ganó dinero? y ¿con qué productos amid perdió dinero?.
 5. ¿Qué productos fué comprado solo por clientes nuevos? y ¿Qué productos fué comprado solo por clientes habtuales?.
