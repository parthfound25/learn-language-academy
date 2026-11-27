-- Public read is intentional: these are reusable lesson recordings, not learner data.
-- Writes are performed server-side with the Supabase service-role key.
insert into storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
values (
  'lesson-audio',
  'lesson-audio',
  true,
  10485760,
  array['audio/mpeg', 'application/json']
)
on conflict (id) do update
set public = excluded.public,
    file_size_limit = excluded.file_size_limit,
    allowed_mime_types = excluded.allowed_mime_types;
