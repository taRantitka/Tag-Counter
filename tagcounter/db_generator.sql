CREATE TABLE reports (site_name TEXT PRIMARY KEY,
                    url TEXT NOT NULL,
                    check_date datetime,
                    report pickle);