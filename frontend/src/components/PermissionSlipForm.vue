<script setup lang="ts">
import type { PermissionSlipData } from './permission-slip-form.types'
import type { PropType } from 'vue'
import merge from 'lodash/merge'
import { VForm } from 'vuetify/components'
import { computed, useTemplateRef, onBeforeMount } from 'vue'
import { defaultFormData } from './default-form-data'

const formData = defineModel('data', {
  type: Object as PropType<PermissionSlipData>,
  default: () => structuredClone(defaultFormData),
})
onBeforeMount(() => {
  const copy: PermissionSlipData = structuredClone(defaultFormData)
  // If we re-assign formData.value the change doesn't get propagated until the next tick (and the
  // form has rendering errors for missing props if the parent didn't pass them). By mutating
  // formData.value in-place, the merged values are available immediately.
  const merged = merge(copy, formData.value)
  merge(formData.value, merged)
})

const valid = defineModel('valid', { type: Boolean, default: false })
const form = useTemplateRef<VForm>('form')
const errors = computed(() => form.value?.errors ?? [])
defineExpose({ errors })

// Validation Rules
function namedRules<T>(
  name: string,
  ruleFunctions: Array<(name: string) => (value: T) => boolean | string>,
): ((value: T) => boolean | string)[] {
  return ruleFunctions.map((f) => f(name))
}

const requiredRule = (name: string) => (value: string | number) => !!value || `${name} is required`
const urlRule = (name: string) => (value: string) =>
  !value || /^https?:\/\//.test(value) || `${name} must be a URL`
const numericRule = (name: string) => (value: number) => !isNaN(value) || `${name} must be a number`
const dollarRule = (name: string) => (value: string) =>
  /^\$?\d+(\.\d{2})?$/.test(value) || `${name} must be a valid dollar amount`
const phoneRule = (name: string) => (value: string) =>
  /^\(\d{3}\)\s?\d{3}-\d{4}$/.test(value) ||
  `${name} must be a valid US phone number: (xxx)xxx-xxxx`
const emailRule = (name: string) => (value: string) =>
  /.+@.+\..+/.test(value) ||
  `${name} must be a valid
email address`
const isoDatetimeRule = (name: string) => (value: string) =>
  !isNaN(Date.parse(value)) || `${name} must be a valid ISO datetime string`
</script>
<template>
  <v-form ref="form" v-model="valid" validate-on="input eager">
    <!-- Images Section -->
    <v-card outlined class="mb-4">
      <v-card-title>Images</v-card-title>
      <v-card-text>
        <v-text-field
          v-model="formData.images.header1"
          label="Header Image URL 1"
          density="compact"
          :rules="namedRules('Header image URL 1', [urlRule])"
        ></v-text-field>
        <v-text-field
          v-model="formData.images.header2"
          label="Header Image URL 2"
          density="compact"
          :rules="namedRules('Header image URL 2', [urlRule])"
        ></v-text-field>
        <v-text-field
          v-model="formData.images.header3"
          label="Header Image URL 2"
          density="compact"
          :rules="namedRules('Header image URL 3', [urlRule])"
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
          :rules="namedRules('Due date', [requiredRule, isoDatetimeRule])"
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
          :rules="namedRules('Camp name', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.url"
          label="Camp URL"
          :rules="namedRules('Camp URL', [requiredRule, urlRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.phone"
          label="Camp Phone"
          :rules="namedRules('Camp Phone', [requiredRule, phoneRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.address"
          label="Camp Address"
          :rules="namedRules('Camp Address', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.camp.site"
          label="Camp Site"
          :rules="namedRules('Camp Site', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-select
          v-model="formData.camp.type"
          label="Camp Type"
          :items="['tent camping', 'cabin camping']"
          :rules="namedRules('Camp Type', [requiredRule])"
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
          :rules="namedRules('Scout Cost', [requiredRule, dollarRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.cost.adult"
          label="Adult Cost"
          :rules="namedRules('Adult Cost', [requiredRule, dollarRule])"
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
          :rules="namedRules('Departure Location', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.departure.time"
          label="Departure Time"
          type="datetime-local"
          :rules="namedRules('Departure Time', [requiredRule, isoDatetimeRule])"
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
          :rules="namedRules('Return Location', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.return.time"
          label="Return Time"
          type="datetime-local"
          :rules="namedRules('Return Time', [requiredRule, isoDatetimeRule])"
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
          :rules="namedRules('Troop Number', [requiredRule, numericRule])"
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
          :rules="namedRules('Coordinator Name', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.coordinator.address"
          label="Coordinator Address"
          :rules="namedRules('Coordinator Address', [requiredRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.coordinator.phone"
          label="Coordinator Phone"
          :rules="namedRules('Coordinator Phone', [requiredRule, phoneRule])"
          density="compact"
        ></v-text-field>
        <v-text-field
          v-model="formData.coordinator.email"
          label="Coordinator Email"
          :rules="namedRules('Coordinator Email', [requiredRule, emailRule])"
          density="compact"
        ></v-text-field>
      </v-card-text>
    </v-card>
  </v-form>
</template>
