# Admin learner activity monitoring

The private **Parth Sharma** account has an **Admin Dashboard** entry in the sidebar. Other accounts continue to use the existing private username/password login configured in Streamlit Secrets. There is no public registration.

## One-time Supabase setup

1. Open the Supabase project SQL Editor.
2. Run the complete contents of `supabase/activity_tracking.sql`.
3. In Streamlit Community Cloud, open App settings → Secrets and add the following server-side section. Use the project's actual URL and the Supabase **service_role** key.

```toml
[supabase]
url = "https://YOUR_PROJECT.supabase.co"
service_role_key = "YOUR_SERVICE_ROLE_KEY"
```

Never put the service-role key in GitHub, source code, or browser-side code. The new tables have RLS enabled and deny ordinary anon/authenticated client access; only the trusted Streamlit server uses the service-role key.

## Learner accounts

Continue to manage accounts in the existing `[users]` section of Streamlit Secrets. Keep the administrator username exactly **Parth Sharma**. Add one username/password entry per learner. Learners do not get access to the Admin Dashboard.

## What is recorded

- Login time, explicit logout time, last heartbeat, session duration and session status.
- A heartbeat approximately every 60 seconds while the app is open.
- Unexpectedly closed sessions are marked timed out after three minutes without a heartbeat. Their recorded duration ends at the last heartbeat.
- Per-language XP, completed lesson IDs, active lesson, practice-round count, correct answers, total answers and achievements.
- Lesson-completion events and practice-round results, including score, accuracy and XP earned.
- Progress snapshots are restored when a learner returns, so the new tracking also makes progress durable across browser sessions.

Session duration measures elapsed time while the app remains open, including idle reading time; it is not a measure of attention. A browser/device sleep or network interruption may cause the session to time out at its last heartbeat.

## Important historical limitation

This tracking starts after the SQL migration and Streamlit Secrets are configured. The old app kept progress in Streamlit session state only, so historical logins, time spent and practice events cannot be reconstructed retroactively. Existing in-memory progress can be captured as the new app saves snapshots, but no earlier session history is available.

## Verification checklist

- Sign in as Parth Sharma and confirm Admin Dashboard appears.
- Sign in as a learner and confirm Admin Dashboard is absent.
- Complete a lesson and submit a practice round.
- Sign out and confirm the session's login, logout and duration are recorded.
- Close a learner tab without signing out, wait at least three minutes, then refresh the admin dashboard to see the session marked timed out.
- Sign back in as the learner and confirm lessons, XP and practice totals are restored.
