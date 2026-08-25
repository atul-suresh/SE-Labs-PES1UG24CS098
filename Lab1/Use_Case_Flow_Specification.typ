#set page(
  paper: "a4",
  margin: (x: 18mm, y: 14mm)
)

#set text(
  font: "Arial",
  size: 10pt
)

#set par(
  leading: 0.6em
)

#align(center)[
  #text(size: 16pt, weight: "bold")[
    Use-Case Flow Specification
  ]

  #v(3pt)

  #text(size: 11pt, weight: "bold")[
    Smart Parking Space Rental & License Validator
  ]
]

#v(8pt)

#table(
  columns: (1.4fr, 4fr),
  inset: 5pt,
  stroke: 0.5pt,

  [*Use Case ID*], [UC-03],
  [*Use Case Name*], [Validate Vehicle Reservation],
  [*Primary Actor*], [Vehicle Owner],
  [*Supporting Actor*], [Parking Warden],
  [*Goal*], [Validate the arriving vehicle against an active parking reservation before allowing entry.]
)

#v(8pt)

== Preconditions

1. The vehicle has arrived at the parking facility entrance.
2. The gate camera and license-plate validation service are operational.
3. The parking reservation database is accessible.

== Postconditions

1. For a valid reservation, the vehicle entry time is recorded.
2. An active parking session is created and the vehicle is permitted to enter.

== Main Success Scenario

1. The Vehicle Owner arrives at the parking entrance.
2. The system captures the vehicle license plate using the gate camera.
3. The system reads the detected license-plate number.
4. The system searches for an active reservation associated with the license plate.
5. The system verifies that the reservation is valid for the current date and time.
6. The system records the vehicle entry time.
7. The system activates the corresponding parking session.
8. The system permits the vehicle to enter the parking facility.

== Alternate Flow — A1: Invalid or Missing Reservation

1. At Step 4 or Step 5, the system determines that no valid active reservation exists.
2. The system marks the vehicle-entry validation as unsuccessful.
3. The vehicle is flagged for review.
4. The Parking Warden is notified of the failed validation.
5. Entry is denied unless the Parking Warden performs an authorized manual review.
