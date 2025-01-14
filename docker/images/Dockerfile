# Usar la imagen oficial de Odoo
FROM odoo:17.0

# Establecer el directorio de trabajo
WORKDIR /opt/odoo

# Copiar los addons personalizados desde la carpeta local 'addons' a la carpeta correspondiente en el contenedor
COPY ../../addons /mnt/extra-addons

# Establecer permisos para los addons
RUN chown -R odoo:odoo /mnt/extra-addons

# Exponer el puerto en el que Odoo escucha
EXPOSE 8069

# Comando para iniciar Odoo
CMD ["odoo"]
