# Configuración del Repositorio de GitHub

Este documento muestra los pasos llevados a cabo para configurar el repositorio de GitHub mediante la creación de claves SSH, la personalización del perfil y la activación de medidas de seguridad adicionales.

## Creación y asociación de claves SSH

Las claves SSH permiten una comunicación segura entre la máquina local y GitHub, eliminando la necesidad de ingresar las credenciales cada vez que interactúas con el repositorio.

1. **Generación de la clave SSH:**
   
   ![Creación de la ssh key](../imgs/create_ssh_key.GIF)

   *En esta imagen, se muestra cómo generar una nueva clave SSH utilizando Git Bash.*

2. **Adición de la clave SSH:**
   
   ![Añadir ssh key al repositorio](../imgs/add_ssh_key.GIF)

   *Aquí se ilustra cómo agregar la clave SSH recién creada al agente SSH.*

## Configuración del nombre y del correo electrónico para que aparezcan en los commits

![Configurar nombre y email](../imgs/config_name_email.GIF)

*Esta imagen muestra cómo establecer tu nombre completo y correo electrónico a nivel global en Git.*

## Edición del Perfil de GitHub

![Edición del Perfil de Github](../imgs/repo_user_info.GIF)

*En esta captura se evidencia el proceso de edición del perfil donde se ha agregado la imagen, el nombre completo, la ubicación y la universidad.*

## Activar Segundo Factor de Seguridad

Para proteger la cuenta de GitHub se ha habilitado la autenticación de dos factores (2FA) a través de una aplicación.

![Activar Segundo factor de Seguridad](../imgs/two_factor_auth.GIF)

*La imagen ilustra que se ha configurado el método de dos pasos mediante una aplicación de autenticación.*

## Documentación Adicional
1. [Milestones](milestones.md)
2. [Historias de Usuario](hu.md)
3. [Descripción detallada del proyecto](../hito1.md)
4. [Inicio](../../README.md)
