<template>
  <v-container>
    <v-form ref="form" v-model="valid">
      <!-- Images Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Images</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.images.header1"
            label="Header 1 Image URL"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.images.header2"
            label="Header 2 Image URL"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.images.header3"
            label="Header 3 Image URL"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Camp Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Camp Information</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.camp.name"
            label="Camp Name"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.camp.url"
            label="Camp URL"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.camp.phone"
            label="Camp Phone"
            :rules="[requiredRule, phoneRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.camp.address"
            label="Camp Address"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.camp.site"
            label="Camp Site"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.camp.type"
            label="Camp Type"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-switch v-model="formData.camp.messkits" label="Messkits Provided"></v-switch>
          <v-text-field
            v-model="formData.camp.map"
            label="Map Image URL"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Cost Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Cost Information</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.cost.scout"
            label="Scout Cost"
            :rules="[requiredRule, dollarRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.cost.adult"
            label="Adult Cost"
            :rules="[requiredRule, dollarRule]"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Departure Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Departure Information</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.departure.location"
            label="Departure Location"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.departure.time"
            label="Departure Time"
            type="datetime-local"
            :rules="[requiredRule, isoDatetimeRule]"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Return Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Return Information</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.return.location"
            label="Return Location"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.return.time"
            label="Return Time"
            type="datetime-local"
            :rules="[requiredRule, isoDatetimeRule]"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Troop Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Troop Information</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.troop.number"
            label="Troop Number"
            :rules="[requiredRule, numericRule]"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Coordinator Section -->
      <v-card outlined class="mb-4">
        <v-card-title>Coordinator Information</v-card-title>
        <v-card-text>
          <v-text-field
            v-model="formData.coordinator.name"
            label="Coordinator Name"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.coordinator.address"
            label="Coordinator Address"
            :rules="[requiredRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.coordinator.phone"
            label="Coordinator Phone"
            :rules="[requiredRule, phoneRule]"
            size="small"
            density="compact"
          ></v-text-field>
          <v-text-field
            v-model="formData.coordinator.email"
            label="Coordinator Email"
            :rules="[requiredRule, emailRule]"
            size="small"
            density="compact"
          ></v-text-field>
        </v-card-text>
      </v-card>

      <!-- Submit Button -->
      <v-btn :disabled="!valid" color="primary" @click="submit">Submit</v-btn>
    </v-form>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useLocalStorage } from '@vueuse/core'

const valid = ref(false)
const formData = useLocalStorage('form-data', {
  images: {
    header1: '',
    header2: '',
    header3: '',
  },
  camp: {
    name: '',
    url: '',
    phone: '',
    address: '',
    site: '',
    type: '',
    messkits: false,
    map: '',
  },
  cost: {
    scout: '',
    adult: '',
  },
  departure: {
    location: '',
    time: '',
  },
  return: {
    location: '',
    time: '',
  },
  troop: {
    number: '',
  },
  coordinator: {
    name: '',
    address: '',
    phone: '',
    email: '',
  },
})

// Validation Rules
const requiredRule = (value: string | number) => !!value || 'This field is required'
const numericRule = (value: number) => !isNaN(value) || 'Must be a number'
const dollarRule = (value: string) =>
  /^\$?\d+(\.\d{2})?$/.test(value) || 'Must be a valid dollar amount'
const phoneRule = (value: string) =>
  /^\(\d{3}\)\s?\d{3}-\d{4}$/.test(value) || 'Must be a valid US phone number: (xxx)xxx-xxxx'
const emailRule = (value: string) => /.+@.+\..+/.test(value) || 'Must be a valid email address'
const isoDatetimeRule = (value: string) =>
  !isNaN(Date.parse(value)) || 'Must be a valid ISO datetime string'

const submit = () => {
  console.log(formData.value)
  // Convert formData to YAML if needed, and submit or process it.
}
</script>
