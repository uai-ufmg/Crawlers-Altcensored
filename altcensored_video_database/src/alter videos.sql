-- SQLite
ALTER TABLE videos ADD COLUMN youtube_user text;
ALTER TABLE videos ADD COLUMN youtube_channel text;
ALTER TABLE videos ADD COLUMN youtube_video text;
ALTER TABLE videos ADD COLUMN views text;
COMMIT;
