---
slug: /integrations/supabase
title: Supabase
description: Learn how to connect your Dreamflow app with Supabase to enable powerful backend features such as authentication, databases, storage, and more.
tags: [Supabase, Integration, Dreamflow, Backend]
sidebar_position: 2
toc_max_heading_level: 4
keywords: [Supabase, Integration, Dreamflow, Backend]
---

# Supabase

Dreamflow makes it easy to integrate [Supabase](https://supabase.com/) into your app with a guided, step-by-step setup. This process connects your project to Supabase, sets up a database, generates client code, and deploys schemas, all without manual setup.

## 1. Connection

The first step is to connect Dreamflow with your Supabase account so it can create new Supabase projects or link to existing ones.

To begin, open the **Supabase** module in Dreamflow and click **Connect to Supabase**. A Supabase authentication window will appear where you can sign in and review the requested permissions. Next, select an organization and click **Authorize Dreamflow**. These permissions allow Dreamflow to create and manage projects, configure database schemas, and generate API keys on your behalf. 

Once complete, Dreamflow will confirm the connection with a **Connected** status.

<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/QvHPsdxLUubTQDPXrxfL?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

## 2. Project Setup

After connecting your Supabase account, the next step is to set up a Supabase project, which will serve as the backend for your app. You can do this in two ways:

- **Select an existing Supabase project:** Choose from the list of your existing Supabase projects.

![select-from-existing-supabase-project.avif](imgs/select-from-existing-supabase-project.avif)

- **Create a new Supabase project:** Let Dreamflow automatically create and configure a new Supabase project for you.

![create-new-supabase-project.avif](imgs/create-new-supabase-project.avif)

**During new project creation:**

- Dreamflow provisions a new project in Supabase, generating a **Project Name**, **Project ID**, **API URL**, and **Anon Key**.
- The database is automatically initialized, giving you a fully configured backend environment.
- All credentials are securely linked to your Dreamflow project, allowing you to start building immediately.

This setup may take a few minutes while Dreamflow provisions the resources and configures your database.

:::info

You can quickly jump into your Supabase dashboard using the **Open in Supabase** button.

:::

## 3. Generate Client Code

Once the project setup is complete, click **Generate Client Code** to let Dreamflow automatically create ready-to-use Supabase integration code tailored to your app. This step eliminates most of the manual setup by wiring your app directly to Supabase with authentication, data models, and database operations.

![generate-client-code-supabase.avif](imgs/generate-client-code-supabase.avif)

### Code Generation Breakdown

When you trigger code generation, Dreamflow performs several background steps, including (but not limited to):

- **Supabase Configuration**:
    - Add the `supabase_flutter` dependency and update `main.dart` for initialization.
    - Generate a `supabase_config.dart` file with project credentials (API URL, Anon Key) and helper functions for database access.
- **Database Schema (`supabase_tables.sql`)**:
    - Define the necessary tables for your app (e.g., users, core data entities, relationships).
    - Add indexes and constraints for efficient queries.
- **Security Policies (`supabase_policies.sql`)**:
    - Enable **Row Level Security (RLS)** across all tables.
    - Generate policies so users can only access their own data, and operations are protected by authentication checks.
- **Service Layer**:
    - Create service classes (e.g., `_service.dart`) with CRUD operations, query helpers, and error handling.
    - Include support for real-time updates, history tracking, or analytics if applicable.
- **Models & Data**:
    - Update models to support Supabase JSON serialization (`fromJson`, `toJson`).
    - Refresh sample data to match the generated schema.
    - Adjust widgets or UI components to bind live data instead of placeholders.
- **App Integration**:
    - Replace hardcoded logic with Supabase-powered queries.
    - Wire authentication, database syncing, and state management into the app flow.

By the end of this step, your app will be fully integrated with Supabase, ready to authenticate users, persist data securely, and sync changes in real time with proper RLS policies in place.

## 4. Schema Deployment

The final step is to deploy your database schema changes to Supabase. You’ll see a list of generated **Migration Files** under the **Schema Deployment** menu (in the left side panel). Follow these steps to apply them in the correct order:

1. **Deploy Tables:** Select the table migration file (i.e., `lib/supabase/supabase_tables.sql`) and click **Deploy Schema Changes**. This will create all the required database tables, along with their defined columns, relationships, and constraints, as specified in your generated schema.
2. **Deploy Policies:** Once the tables are successfully created, select the policy migration file (i.e., `lib/supabase/supabase_policies.sql`) and click **Deploy Schema Changes**. This will enable **Row Level Security (RLS)** on your tables and apply access control policies that restrict data operations to authenticated users. For example, users will only be able to view, insert, update, or delete their own records in the `users` and other tables, ensuring that each user can access only their personal data within the app.

:::info

After the initial setup, any new updates or modifications you make will be added to the `pending_migrations.sql` file. You only need to deploy these new migrations; previously deployed tables and policies do not need to be redeployed.

:::


<div style={{
    position: 'relative',
    paddingBottom: 'calc(52.67989417989418% + 41px)', // Keeps the aspect ratio and additional padding
    height: 0,
    width: '100%'}}>
    <iframe 
        src="https://demo.arcade.software/99SOvWJi7ICY3REWYU3d?embed&show_copy_link=true"
        title=""
        style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            colorScheme: 'light'
        }}
        frameborder="0"
        loading="lazy"
        webkitAllowFullScreen
        mozAllowFullScreen
        allowFullScreen
        allow="clipboard-write">
    </iframe>
</div>
<p></p>

## Add Sample Data to Supabase

Dreamflow lets you add sample data to your Supabase project for easier development and testing. The generated data follows your app’s schema, allowing you to quickly verify how your app behaves with populated tables.


To add sample data from Dreamflow, go to the **Supabase > Sample Data**, and follow the instructions below:

- **For Apps with Login Functionality:** First, sign up in your app using an email and password. After logging in, enter the same email address in the **User Email** field and click **Create Sample Data**. This will generate sample records linked to that user account.

    ![add-sample-data-supabase-with-login.avif](imgs/add-sample-data-supabase-with-login.avif)

- **For Apps without Login Functionality:** You can skip the email step, as it’s optional. Simply click **Create Sample Data** to generate test records directly in your Supabase database.

    ![add-sample-data-supabase-without-login.avif](imgs/add-sample-data-supabase-without-login.avif)

:::warning

You can only generate sample data **once** per project. If you need to modify or remove the sample data later, you can do so directly from the **Supabase** **Table Editor**.

:::

## FAQs

<details>
<summary>
Why can’t I sign up with Supabase Authentication? 
</summary>

<p>
If you are unable to sign up in the generated Supabase authentication code, it’s likely due to **Supabase authentication settings**. By default, Supabase requires **email confirmation** for new accounts. This means that sign-ups using invalid or dummy email addresses will fail.

To fix this, use a valid email address during sign-up so you can receive and confirm the verification email.
</p> 
</details>



<details>
<summary>
Are Supabase Edge Functions supported in Dreamflow? 
</summary>

<p>
Currently, **Edge Functions are not supported in Dreamflow**. If you need to create or manage Edge Functions, you’ll have to do so directly from the **Supabase Console**.
</p> 
</details>

<details>
<summary>
Why can’t I log in with the email I used to generate sample data? 
</summary>

<p>
If you generated sample data before adding authentication to your app, logging in with that same email will fail — and this is expected behavior.

When sample data is created, it inserts records directly into the Supabase database, including user details, but it doesn’t go through the actual authentication process. As a result, those users exist in the database but don’t have valid authentication credentials in Supabase Auth.

To fix it, you can delete the dummy user record from the Auth table and then sign up again in your app with that email.
</p> 
</details>