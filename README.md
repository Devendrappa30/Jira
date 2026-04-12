🚀 JIRA SETUP & IMPLEMENTATION – STEP BY STEP (ORDER WISE)

🟢 PHASE 1 – PRE-IMPLEMENTATION (Before Touching Jira)
1️⃣ Requirement Gathering (Most Important Step)
Define:
What type of project?
Software Development
ITSM / Service Desk
Business Project
Team size?
Roles?
Workflow stages?
SLA required?
Integrations needed?
Migration required?
Deliverable:
Process document
Role matrix
Workflow diagram
Field requirement list
Migration plan (if applicable)


🟢 PHASE 2 – SYSTEM INITIAL CONFIGURATION (Global Setup)
Go to: ⚙ Jira Admin → System Settings

🔹 2.1 General Configuration
Configure:
Site Title
Default Language
Default Timezone
Email From Name
Indexing Language
📌 These are foundational system-level settings 
Jira Implementation Guide

🔹 2.2 Look & Feel (Branding)



4
Configure:
Logo
Site Title
Favicon
Navigation Colors
Date Format
ISO Standard
Announcement Banner (for maintenance)



🔹 2.3 Global Permissions Setup
Go to: System → Global Permissions
Define:
Administer Jira
Browse Users
Share Dashboards
Bulk Changes (restrict carefully ⚠)
Create Team-Managed Projects
📌 Best Practice: Assign to Groups, not individuals 
Jira Implementation Guide

🔹 2.4 Create Groups
Example:
jira-admins
developers
qa-team
project-managers
stakeholders





🟢 PHASE 3 – SPACE (PROJECT) LEVEL SETUP

🔹 3.1 Create Space / Project
Choose:
Company-managed (Recommended for enterprise control)
Team-managed (For autonomy)
Define:
Name
Key
Template (Scrum / Kanban / Service)

🔹 3.2 Configure Space Roles
From your guide, default roles include:
Administrators
Developer
QA
Project Manager
Business Stakeholder
Service Desk Team (Do NOT delete) Jira Implementation Guide 
Map:
Groups → Roles → Permission Scheme



🔹 3.3 Permission Scheme Setup
Define permissions:
Browse
Create
Edit
Transition
Assign
Add Comments
Delete
Issue Security
Use Permission Helper for testing 
Jira Implementation Guide









🟢 PHASE 4 – WORKFLOW DESIGN

🔹 4.1 Define Workflow Stages
Example (Software Scrum):
To Do → In Progress → Code Review → QA → Done
Example (ITSM):
Open → Assigned → In Progress → Pending → Resolved → Closed
🔹 4.2 Configure:
Status
Transitions
Validators
Conditions
Post Functions
Screens

🔹 4.3 Map Workflow to Issue Types
Bug
Task
Story
Epic
Service Request
Incident



🟢 PHASE 5 – FIELDS & SCREENS

🔹 5.1 Create Custom Fields
Example:
Severity
Root Cause
Environment
Deployment Date
Business Impact

🔹 5.2 Screen Scheme Mapping
Map:
Create Screen
Edit Screen
View Screen







🟢 PHASE 6 – NOTIFICATION CONFIGURATION

🔹 6.1 Notification Scheme
Define who gets notified:
Reporter
Assignee
Watchers
Project Role

🔹 6.2 Email Setup
Check:
Outgoing Mail (Enable in Prod)
Disable during migration/bulk update ⚠ Jira Implementation Guide 

🔹 6.3 Alert Configuration (For ITSM)



4
Configure:
Email alerts
SMS
Voice
Mobile push
Quiet hours
Escalation rules Jira Implementation Guide 

🟢 PHASE 7 – AUTOMATION

🔹 7.1 Create Automation Rules
Structure:
Trigger → Condition → Action
Example:
When issue created → Assign to team lead
When moved to Done → Notify stakeholders
When Severity = Critical → Send escalation email
Use:
Templates
Global rules
Audit log for troubleshooting Jira Implementation Guide 







🟢 PHASE 8 – DASHBOARDS & REPORTING

🔹 8.1 Default Dashboard Setup



4
Add gadgets:
Filter Results
Pie Chart
Two-Dimensional Filter
Recently Created Chart
Ensure:
Filters are shared properly
Projects exist (avoid invalid project ID errors) Jira Implementation Guide 






🟢 PHASE 9 – IMPORT / MIGRATION (If Required)

🔹 9.1 Cloud to Cloud
Order:
Take backup
Import Data (.xml)
Import Media
Validate users
Validate permissions
⚠ Import overwrites data 
Jira Implementation Guide

🔹 9.2 Server to Cloud
Use: Jira Cloud Migration Assistant (JCMA) 
Jira Implementation Guide
Site Import is discontinued.

🔹 9.3 CSV Import (Most Common)
Steps:
Clean data
Map fields carefully
Test in sandbox
Validate workflow mapping

🟢 PHASE 10 – SECURITY & GOVERNANCE

🔹 10.1 Audit Log
Used for:
Permission changes
Workflow edits
User creation
Compliance audits Jira Implementation Guide 

🔹 10.2 Backup Strategy
Take periodic manual backups
Include attachments
Store securely
Document restore procedure Jira Implementation Guide 

🔹 10.3 Email Monitoring
Use:
Admin Email Audit
Monitor failed emails
Check Free plan email limits Jira Implementation Guide 



🟢 PHASE 11 – GO LIVE CHECKLIST
Before Go Live:
✅ Permissions tested ✅ Workflows tested ✅ Automation tested ✅ Email tested ✅ Dashboards validated ✅ Migration validated ✅ Backup taken ✅ Announcement banner configured

🟢 PHASE 12 – POST GO-LIVE SUPPORT
After launch:
Monitor Audit Log
Monitor Automation usage
Monitor Email failures
Fine tune notification scheme
Review bulk change permissions
Optimize performance






🎯 START → END SUMMARY FLOW


Requirement Gathering
↓
System Global Setup
↓
Create Groups
↓
Create Project
↓
Configure Roles
↓
Configure Permissions
↓
Design Workflow
↓
Create Fields & Screens
↓
Setup Notifications
↓
Setup Automation
↓
Create Dashboards
↓
Test Everything
↓
Migration (if needed)
↓
Take Backup
↓
Go Live
↓
Monitor & Optimize
