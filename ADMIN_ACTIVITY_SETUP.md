# Admin learner activity monitoring

The dedicated **Admin** username has access to the Admin Dashboard. The separate **Parth Sharma** account is an ordinary learner account and appears in learner activity reports like other learners. Role assignment is based on the login username, not a person's display name.

## Configure private accounts in Streamlit Secrets

Keep all accounts in the existing `[users]` section. Add the administrator account and your learner accounts there. For example:

```toml
[users]
Admin = "SET_THE_ADMIN_PASSWORD_IN_STREAMLIT_SECRETS"
"Parth Sharma" = "SET_PARTHS_LEARNER_PASSWORD"
"Learner 2" = "SET_LEARNER_PASSWORD"
```

Use your chosen passwords directly in Streamlit Community Cloud → App settings → Secrets. Do not put real passwords in GitHub, source files, screenshots, or messages. The exact login username **Admin** is the only account with administrator access. Enter the username with this exact capitalization. The username **Parth Sharma** is a normal learner.

There is no public registration.

## One-time Supabase setup

1. Open the Supabase project SQL Editor.
2. Run the complete contents of `supabase/activity_tracking.sql`.
3. In Streamlit Community Cloud, open App settings → Secrets and add this server-side section, using the actual project URL and Supabase **service_role** key:

```toml
[supabase]
url = "https://YOUR_PROJECT.supabase.co"
service_role_key = "YOUR_SERVICE_ROLE_KEY"
```

Never put the service-role key in GitHub, source code, or browser-side code. The new tables have RLS enabled and deny ordinary anon/authenticated client access; only the trusted Streamlit server uses the service-role key.

## What is recorded

- Login time, explicit logout time, last heartbeat, session duration and session status.
- A heartbeat approximately every 60 seconds while the app is open.
- Unexpectedly closed sessions are marked timed out after three minutes without a heartbeat. Their recorded duration ends at the last heartbeat.
- Per-language XP, completed lesson IDs, active lesson, practice-round count, correct answers, total answers and achievements.
- Lesson-completion events and practice-round results, including score, accuracy and XP earned.
- Progress snapshots are restored when a learner returns, so progress is durable across browser sessions.

Session duration measures elapsed time while the app remains open, including idle reading time; it is not a measure of attention. A browser/device sleep or network interruption may cause the session to time out at its last heartbeat.

## Important historical limitation

Tracking starts after the SQL migration and Streamlit Secrets are configured. Earlier login/logout and practice event history cannot be reconstructed retroactively.

## Verification checklist

- Sign in as **Admin** and confirm Admin Dashboard appears.
- Sign in as **Parth Sharma** and confirm Admin Dashboard is absent.
- Confirm Parth Sharma appears as a learner in Admin Dashboard.
- Complete a lesson and submit a practice round as a learner.
- Sign out and confirm the session's login, logout and duration are recorded.
- Close a learner tab without signing out, wait at least three minutes, then refresh the admin dashboard to see the session marked timed out.
- Sign back in as the learner and confirm lessons, XP and practice totals are restored.
