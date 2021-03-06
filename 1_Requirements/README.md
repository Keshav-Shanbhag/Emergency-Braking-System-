# Requirements
## Introduction
 * The project aims to design and develop the vehicle with emergency braking system to avoid collision.
 * It senses the obstacle in the environment using ultrasonic sensor and send input to Raspberry Pi.
 * It sends a mail and sms about location of the vehicle to the nearest Police station where the accident happened.

## Research
 * In 1996,Merceds-Benz became the first company to make Brake Assist standard equipment on all its models.
 * In 2007,European commision announced that it wanted Brake Assit to be included on all new models sold in the EU .
 * This brake assist regulation is not used in the united states because the unitd states do not use UNECE regulations.
 * In India,Emergency Braking system was not introduced which may be enforced in 2023.
 
## Cost and Features and Timeline
### Cost
  * The system can be adopted in any vehicle and less costs.

### Features
   * System comes with autonomous braking system with feature to send sms/mail alert to nearby police
     station if any oposite vehicle hits the system.
### Timeline
   * System can work with all models of vehicles and different road types.

## Defining Our System

    * The main purpose is to design the automatic braking system in order to avoid the accident.
## SWOT ANALYSIS
### Strength
  * avoids collision
  * send alert to help

### Weakness
  * Accident happens if opposite vehicle hits.

### Opportunity
  * Helps to reduce Accidents

### Threats
  * If any obstacles other than front side ,system not detects obstacles.

# 4W&#39;s and 1&#39;H

## Who:

 * For Driver who cannot able to control vehicle in some circumstances.

## What:

 * Emergency Braking system helps to avoid accidents of vehicle when Driver cannot control vehicle.

## When:

 * It used in cases where Driver fails to apply brakes and finds obstacles ,then this system will stop the vehicle.

## Where:

* Used in the vehicle to avoid accidents.

## How:

* This system finds front obstacles and if driver wont apply brakes ,immediately vehicle gets stopped.This prevents collision.

# Detail requirements
## High Level Requirements:

|      ID          |Description                          |Status                         |
|----------------|-------------------------------|-----------------------------|
|HR_01|Obstacle Detection |Implemented|
|HR_02|Emergency Brake|Implemented|
|HR_03|Email Notification|Implemented|
|HR_04|SMS Alert |Implemented|
|HR_05|Driver Authentication |Implemented|
|HR_06|Location |Future|




##  Low level Requirements:
|      ID          |Description                          |Status                         |
|----------------|-------------------------------|-----------------------------|
|LR_01|Sensor Working|Implemented|
|LR_02|Motor Functioning|Implemented|
|LR_03|Vehicle Stopping|Implemented|
|LR_04|Vehicle Starting |Implemented|
|LR_05|LED working|Implemented|
|LR_06|Working with Dirty Roads|Implemented|
|LR_07|Power Backup|Implemented|
|LR_08|Control through App|Implemented|

