# Gunakan base image PHP dengan server built-in
FROM php:8.2-apache

# Salin file index.php ke dalam direktori root web server
COPY . /var/www/html/

# Atur permission untuk memastikan file dapat diakses
RUN chown -R www-data:www-data /var/www/html/

# Expose port 80
EXPOSE 80

