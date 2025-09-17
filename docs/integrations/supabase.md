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

## 1. Connection and Project Setup

The first step is to connect Dreamflow with your Supabase account and set up a project.

To begin, open the **Supabase** tab in Dreamflow and click **Connect to Supabase**. A Supabase authentication window will appear where you can sign in and review the requested permissions. Next, select an organization and click **Authorize Dreamflow**. These permissions allow Dreamflow to create and manage projects, configure database schemas, and generate API keys on your behalf. 

After connecting, Dreamflow automatically creates a new Supabase project and links it to your app. This sets up the backend infrastructure and database for your project. Specifically:

- A new project is provisioned in Supabase with a **Project Name**, **Project ID**, **API URL**, and **Anon Key**.
- Dreamflow initializes the database, ensuring you have a ready-to-use backend.
- These details are securely linked back to your Dreamflow project so you can start building right away.

This setup may take a few minutes while Dreamflow provisions the resources and configures your database.

:::info

You can quickly jump into your Supabase dashboard using the **Open in Supabase** button.

:::


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


## 2. Generate Client Code

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

## 3. Schema Deployment

The final step is to deploy your database schema changes to Supabase. To do so, just click **Deploy Schema Changes**. During this process:

- Dreamflow applies your generated schema, including tables, relationships, constraints, and security policies, directly to your Supabase project.
- As part of deployment, Dreamflow can run migrations and update your live database structure. You can review `pending_migrations.sql` beforehand to see exactly what changes will be applied.

Once deployed, your Supabase backend is live. Users can sign up, authenticate, and their data will automatically sync to the cloud with Row Level Security (RLS) and policies enforced to protect privacy.

:::warning

Schema deployment is an ongoing process. Any time you modify tables, relationships, or security rules in Dreamflow, you’ll need to redeploy to keep your Supabase project up to date.

:::

![deploy-schema-changes.avif](imgs/deploy-schema-changes.avif)