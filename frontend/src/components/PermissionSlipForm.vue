<script setup lang="ts">
import { ref } from 'vue'
import { useLocalStorage, watchDebounced } from '@vueuse/core'

const emit = defineEmits(['update'])

const valid = ref(false)

const formData = useLocalStorage('form-data', {
  images: {
    header1: '',
    header2: '',
    header3: '',
  },
  dueDate: '',
  camp: {
    name: '',
    url: '',
    phone: '',
    address: '',
    site: '',
    type: 'tent camping',
    messkits: true,
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

watchDebounced(
  formData,
  () => {
    if (valid.value) {
      emit('update', formData.value)
    } else {
      console.log('Form not valid')
    }
  },
  { debounce: 500, maxWait: 5_000, deep: true, immediate: true },
)

// Validation Rules
const requiredRule = (value: string | number) => !!value || 'This field is required'
const urlRule = (value: string) => !value || /^https?:\/\//.test(value) || 'Must be a URL'
const numericRule = (value: number) => !isNaN(value) || 'Must be a number'
const dollarRule = (value: string) =>
  /^\$?\d+(\.\d{2})?$/.test(value) || 'Must be a valid dollar amount'
const phoneRule = (value: string) =>
  /^\(\d{3}\)\s?\d{3}-\d{4}$/.test(value) || 'Must be a valid US phone number: (xxx)xxx-xxxx'
const emailRule = (value: string) => /.+@.+\..+/.test(value) || 'Must be a valid email address'
const isoDatetimeRule = (value: string) =>
  !isNaN(Date.parse(value)) || 'Must be a valid ISO datetime string'
</script>
<template>
  <v-form ref="form" v-model="valid">
    <!-- Images Section -->
    <v-card outlined class="mb-4">
      <v-card-title>Images</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="formData.images.header1"
          label="Header 1 Image URL"
          density="compact"
          :rules="[urlRule]"
        ></v-text-field>
        <v-text-field
          v-model="formData.images.header2"
          label="Header 2 Image URL"
          density="compact"
          :rules="[urlRule]"
        ></v-text-field>
        <v-text-field
          v-model="formData.images.header3"
          label="Header 3 Image URL"
          density="compact"
          :rules="[urlRule]"
        ></v-text-field>
      </v-card-text>
    </v-card>

    <v-card outlined class="mb-4">
      <v-card-title>Due date</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="formData.dueDate"
          label="Due date"
          type="date"
          :rules="[requiredRule, isoDatetimeRule]"
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
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.url"
          label="Camp URL"
          :rules="[requiredRule, urlRule]"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.phone"
          label="Camp Phone"
          :rules="[requiredRule, phoneRule]"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.address"
          label="Camp Address"
          :rules="[requiredRule]"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.site"
          label="Camp Site"
          :rules="[requiredRule]"
          density="compact"
        ></v-text-field>
        <v-select
          v-model="formData.camp.type"
          label="Camp Type"
          :items="['tent camping', 'cabin camping']"
          :rules="[requiredRule]"
          density="compact"
        ></v-select>
        <v-switch v-model="formData.camp.messkits" label="Messkits Required"></v-switch>
        <v-text-field
          v-model="formData.camp.map"
          label="Map Image URL"
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
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.cost.adult"
          label="Adult Cost"
          :rules="[requiredRule, dollarRule]"
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
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.departure.time"
          label="Departure Time"
          type="datetime-local"
          :rules="[requiredRule, isoDatetimeRule]"
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
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.return.time"
          label="Return Time"
          type="datetime-local"
          :rules="[requiredRule, isoDatetimeRule]"
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
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.coordinator.address"
          label="Coordinator Address"
          :rules="[requiredRule]"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.coordinator.phone"
          label="Coordinator Phone"
          :rules="[requiredRule, phoneRule]"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.coordinator.email"
          label="Coordinator Email"
          :rules="[requiredRule, emailRule]"
          density="compact"
        ></v-text-field>
      </v-card-text>
    </v-card>
  </v-form>
</template>
