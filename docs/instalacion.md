
sudo -u postgres psql
\c odoo_db
UPDATE res_users SET password = '1234' WHERE login = 'admin';