<script setup lang="ts">
import { ref } from 'vue'
import PermissionSlipForm from '@/components/PermissionSlipForm.vue'
import fetchival from 'fetchival'

const pdfSrc = ref(null)

async function handleUpdate(e) {
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
        <PermissionSlipForm @update="handleUpdate"></PermissionSlipForm>
      </v-col>
      <v-col v-if="pdfSrc">
        <v-btn
          color="primary"
          class="mt-4"
          :href="pdfSrc"
          download="permission-slip.pdf"
          target="_blank"
        >
          Download PDF
        </v-btn>
        <iframe :src="pdfSrc" width="100%" height="100%" />
      </v-col>
    </v-row>
  </v-container>
</template>
