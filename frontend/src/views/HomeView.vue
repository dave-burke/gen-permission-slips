<script setup lang="ts">
import { ref } from 'vue'
import PermissionSlipForm from '@/components/PermissionSlipForm.vue'
import fetchival from 'fetchival'

const pdfSrc = ref(null)

async function handleSubmit(e) {
  try {
    const response = await fetchival('/api/pdf', { responseAs: 'response' }).post(e)
    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}`)
    }
    console.log(response)
    if (pdfSrc.value) {
      URL.revokeObjectURL(pdfSrc.value)
    }
    pdfSrc.value = URL.createObjectURL(await response.blob())
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
      <v-col v-if="pdfSrc">
        <iframe :src="pdfSrc" width="100%" height="100%" />
      </v-col>
    </v-row>
  </v-container>
</template>
