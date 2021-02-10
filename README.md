# testReactRedux-Vuex-DRF

## Get Started.

## DataBase information.

- users

  - id_profile - Serial (PK)
  - username - Text
  - email - Text
  - createdAt - DateTime
  - is_active - boolean
  - is_staff - boolean

- profile

  - id_profile - Serial (PK)
  - bio - Text
  - image - UrlField

- travels

  - id_travel - Serial (PK)
  - user_id - User (FK)
  - status_id - Status (FK)
  - date - Date
  - origin_location - Text
  - destination_location - Text
  - start_time - Time
  - finish_time - Time
  - price - Float
  - createdAt - DateTime

- status

  - id_status - Serial (PK)
  - name - Text
  - closed - Boolean

- shipping

  - id_shipping - Serial (PK)
  - travel_id - Travel (FK)
  - user_id - User (FK)
  - category_id Category (FK)
  - weight - Integer
  - height - Integer
  - width - Integer
  - depth - Integer
  - createdAt - DateTime

- categories

  - id_category - Serial (PK)
  - name - Text
  - image - Text

- comments

  - id_comment - Serial (PK)
  - user_id - User (FK)
  - travel_id - Travel (FK)
  - message - Text

## Mejoras

### Frontend

1. Store modularized with namespaced, using map ...
2. Toaster implemented at the application level (global store, not per module).
3. Responsive, mobile and desktop version in all components and views (control from App.vue).
4. Search component with autocomplete.


### Backend

1. Relationship 1 to many profile -> travels 