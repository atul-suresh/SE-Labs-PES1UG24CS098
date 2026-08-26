#set page(paper: "a4", margin: (x: 1.7cm, y: 1.5cm))
#set text(size: 10.5pt)
#set par(justify: true, leading: 0.65em)

#align(center)[
  #text(size: 19pt, weight: "bold")[Software Engineering Lab 2]
  #v(4pt)
  #text(size: 14pt, weight: "bold")[Agile Backlog Creation & Sprint Simulation in Jira]
  #v(4pt)
  #text(size: 11pt)[Smart Parking Space Rental & License Validator]
]
#v(8pt)
#text(size: 10.5pt)[Name: Atul Suresh]
#linebreak()
#text(size: 10.5pt)[SRN: PES1UG24CS098]
#linebreak()
#text(size: 10.5pt)[Section: B]

#v(10pt)

= 1. EPICs

The functional requirements identified in Lab 1 were grouped into three major functional themes:

- *Parking Reservation Management*
- *Vehicle Access and Billing*
- *Parking Compliance Monitoring*

#figure(
  image("screenshots/01_EPICs.png", width: 100%),
  caption: [Jira Epic panel showing the three Epics and their completion progress.]
)

#pagebreak()

= 2. Product Backlog and Story Point Assignment

Seven User Stories were created under the Epics, prioritized as High or Medium, and estimated using Fibonacci-style Story Points.

#figure(
  image("screenshots/02_Backlog_User_Stories_Story_Points.png", width: 100%),
  caption: [Jira backlog showing User Stories, Epic associations, priorities, and Story Point estimates.]
)

= 3. Sprint Planning

== Sprint 1
Sprint 1 contained four User Stories with a total estimate of 13 Story Points.

#figure(
  image("screenshots/03_Sprint1_Planning.png", width: 100%),
  caption: [Sprint 1 planning view.]
)

== Sprint 2
Sprint 2 contained three User Stories with a total estimate of 13 Story Points.

#figure(
  image("screenshots/04_Sprint2_Planning.png", width: 100%),
  caption: [Sprint 2 planning view.]
)

#pagebreak()

= 4. Active Sprint Simulation

During the sprint simulation, User Stories were progressed across *To Do*, *In Progress*, and *Done* states.

#figure(
  image("screenshots/05_Active_Sprint_View.png", width: 100%),
  caption: [Active Sprint board showing work distributed across workflow states.]
)

= 5. Burndown Charts

== Sprint 1 Burndown
#figure(
  image("screenshots/06_Sprint1_Burndown.png", width: 100%),
  caption: [Sprint 1 Burndown Chart using Story Points.]
)

== Sprint 2 Burndown
#figure(
  image("screenshots/07_Sprint2_Burndown.png", width: 100%),
  caption: [Sprint 2 Burndown Chart using Story Points.]
)

#pagebreak()

= 6. Reflection

*1. Did your estimations reflect the actual effort?*

The Story Point estimates provided a reasonable relative measure of effort. Simpler stories such as viewing available parking bays were assigned fewer points, while validation, billing, and overstay-related functionality received higher estimates. Since the sprint was simulated within a laboratory session, the estimates represent relative complexity rather than measured implementation time.

*2. Was your backlog well-prioritized?*

Yes. Core reservation, vehicle access, billing, and authorization functionality was assigned High priority where appropriate, while supporting monitoring functionality was assigned Medium priority. This kept the backlog focused on the most important user and system needs.

*3. How did your simulated sprint align with your plan?*

The simulation followed the planned Scrum workflow. User Stories were distributed across two sprints, progressed from To Do to In Progress and Done, and both sprints were completed. The planned scope was therefore completed successfully.

*4. What insights did the burndown chart give about your team's capacity?*

The burndown charts show a sharp reduction in remaining Story Points because the sprint activity was simulated within a short laboratory session. This confirms that the planned work was completed, while also showing that a real sprint would ideally spread completion more gradually across the sprint duration for more meaningful capacity and velocity tracking.

= 7. Final Verification

Both sprints were closed and all seven User Stories were verified as Done.

#figure(
  image("screenshots/08_Final_Verification.png", width: 100%),
  caption: [Terminal verification showing Sprint 1 and Sprint 2 closed and all seven User Stories completed.]
)
