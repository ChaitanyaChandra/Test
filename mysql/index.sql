-- select * from c_logs
-- drop table c_logs 

-- CREATE TABLE c_logs (
--     id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
--     cluster_name VARCHAR(255) NOT NULL,
--     namespace VARCHAR(255) NOT NULL,
--     deployment VARCHAR(255) NOT NULL,
--     container VARCHAR(255) NOT NULL,
--     milli_cpu INT NOT NULL,
--     mb_memory INT NOT NULL,
--     log_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     PRIMARY KEY (id)
-- );

-- INSERT INTO c_logs
--     (cluster_name, namespace, deployment, container, milli_cpu, mb_memory)
-- VALUES
--     ('master', 'chaitanya-chandra-testing', 'demo-deployment-1', 'demo-container', 450, 249),
--     ('master', 'chaitanya-chandra-testing', 'demo-deployment-2', 'demo-container', 500, 250),
--     ('master', 'chaitanya-chandra-testing', 'demo-deployment-2', 'demo-container-two', 600, 256); 

-- INSERT INTO c_logs
--     (cluster_name, namespace, deployment, container, milli_cpu, mb_memory)
-- VALUES
--     ('master', 'chaitanya-chandra-testing', 'demo-deployment-2', 'demo-container-two', 500, 500);

-- SELECT COUNT(*) AS total_records
-- FROM c_logs;

