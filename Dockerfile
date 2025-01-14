# Usa la imagen base de Odoo versión 17
FROM odoo:17.0

# Crea el directorio para los addons personalizados
RUN mkdir -p /mnt/extra-addons

# Copia los addons personalizados desde el contexto del build a la imagen
COPY ./addons /mnt/extra-addons

# Establece las variables de entorno necesarias
ENV HOST=mydb \
    USER=odoo \
    PASSWORD=myodoo

# Define el usuario que ejecutará el contenedor
USER odoo

# Expon el puerto 8069
EXPOSE 8069

# Comando por defecto para ejecutar Odoo
CMD ["odoo"]
