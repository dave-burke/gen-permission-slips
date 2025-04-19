<script setup lang="ts">
import { ref } from 'vue'
import PermissionSlipForm from '@/components/PermissionSlipForm.vue'
import { VPdfViewer } from '@vue-pdf-viewer/viewer'
import fetchival from 'fetchival'

const pdfData = ref(null)

async function handleSubmit(e) {
  // todo post
  try {
    const response = await fetchival('http://localhost:5000/pdf', { responseAs: 'response' }).post(
      e,
    )
    console.log(response)
  } catch (err) {
    console.log(err)
  }
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <PermissionSlipForm @submit="handleSubmit"></PermissionSlipForm>
      </v-col>
      <v-col v-if="pdfData">
        <VPdfViewer :src="pdfData" />
      </v-col>
    </v-row>
  </v-container>
</template>
