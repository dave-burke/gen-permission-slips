<template>
  <v-container class="fill-height">
    <v-responsive class="align-centerfill-height mx-auto" max-width="900">
      <v-form ref="form" v-model="valid">
        <!-- Images Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Images</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.images.header1" label="Header 1 Image URL" required></v-text-field>
            <v-text-field v-model="formData.images.header2" label="Header 2 Image URL" required></v-text-field>
            <v-text-field v-model="formData.images.header3" label="Header 3 Image URL" required></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Camp Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Camp Information</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.camp.name" label="Camp Name" required></v-text-field>
            <v-text-field v-model="formData.camp.url" label="Camp URL" required></v-text-field>
            <v-text-field v-model="formData.camp.phone" label="Camp Phone" required></v-text-field>
            <v-text-field v-model="formData.camp.address" label="Camp Address" required></v-text-field>
            <v-text-field v-model="formData.camp.site" label="Camp Site" required></v-text-field>
            <v-text-field v-model="formData.camp.type" label="Camp Type" required></v-text-field>
            <v-switch v-model="formData.camp.messkits" label="Messkits Provided" required></v-switch>
            <v-text-field v-model="formData.camp.map" label="Map Image URL" required></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Cost Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Cost Information</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.cost.scout" label="Scout Cost" required></v-text-field>
            <v-text-field v-model="formData.cost.adult" label="Adult Cost" required></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Departure Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Departure Information</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.departure.location" label="Departure Location" required></v-text-field>
            <v-text-field v-model="formData.departure.time" label="Departure Time" required
              type="datetime-local"></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Return Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Return Information</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.return.location" label="Return Location" required></v-text-field>
            <v-text-field v-model="formData.return.time" label="Return Time" required
              type="datetime-local"></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Troop Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Troop Information</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.troop.number" label="Troop Number" required></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Coordinator Section -->
        <v-card outlined class="mb-4">
          <v-card-title>Coordinator Information</v-card-title>
          <v-card-text>
            <v-text-field v-model="formData.coordinator.name" label="Coordinator Name" required></v-text-field>
            <v-text-field v-model="formData.coordinator.address" label="Coordinator Address" required></v-text-field>
            <v-text-field v-model="formData.coordinator.phone" label="Coordinator Phone" required></v-text-field>
            <v-text-field v-model="formData.coordinator.email" label="Coordinator Email" required></v-text-field>
          </v-card-text>
        </v-card>

        <!-- Submit Button -->
        <v-btn :disabled="!valid" color="primary" @click="submit">Submit</v-btn>
      </v-form>
    </v-responsive>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useLocalStorage } from '@vueuse/core'

const valid = ref(false);
const formData = useLocalStorage('form-data', {
  images: {
    header1: "",
    header2: "",
    header3: "",
  },
  camp: {
    name: "",
    url: "",
    phone: "",
    address: "",
    site: "",
    type: "",
    messkits: false,
    map: "",
  },
  cost: {
    scout: "",
    adult: "",
  },
  departure: {
    location: "",
    time: "",
  },
  return: {
    location: "",
    time: "",
  },
  troop: {
    number: "",
  },
  coordinator: {
    name: "",
    address: "",
    phone: "",
    email: "",
  },
});

const submit = () => {
  console.log(formData.value);
  // Convert formData to YAML if needed, and submit or process it.
};

</script>
