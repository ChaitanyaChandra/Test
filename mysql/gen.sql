INSERT INTO c_logs
    (cluster_name, namespace, deployment, container, milli_cpu, mb_memory, log_date)
SELECT
    'master' AS cluster_name,

    CONCAT(
        'namespace-',
        LPAD(FLOOR(n / 1000) + 1, 3, '0')
    ) AS namespace,

    CONCAT(
        'deployment-',
        LPAD(FLOOR(MOD(n, 1000) / 10) + 1, 3, '0')
    ) AS deployment,

    CONCAT(
        'container-',
        LPAD(MOD(n, 10) + 1, 2, '0')
    ) AS container,

    -- CPU: 10 to 100 milli CPU
    10 + MOD(n * 37, 91) AS milli_cpu,

    -- Memory: 64 to 300 MB
    64 + MOD(n * 53, 237) AS mb_memory,

    -- Spread records over the last 30 days
    TIMESTAMPADD(
        MINUTE,
        -MOD(n * 7, 43200),
        CURRENT_TIMESTAMP
    ) AS log_date

FROM (
    SELECT
        a.n
        + b.n * 10
        + c.n * 100
        + d.n * 1000
        + e.n * 10000 AS n
    FROM
        (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
         UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) a
    CROSS JOIN
        (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
         UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) b
    CROSS JOIN
        (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
         UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) c
    CROSS JOIN
        (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
         UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) d
    CROSS JOIN
        (SELECT 0 n UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
         UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) e
) numbers
WHERE n < 100000;