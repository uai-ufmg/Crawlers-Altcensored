-- SQLite
delete   from views
where    rowid not in
         (
         select  min(rowid)
         from    views
         group by
                 url
         );

         COMMIT;

CREATE UNIQUE INDEX views_pk
on views (url);