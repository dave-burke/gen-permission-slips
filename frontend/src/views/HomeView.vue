<script setup lang="ts">
import { ref } from 'vue'
import PermissionSlipForm from '@/components/PermissionSlipForm.vue'
import { ofetch } from 'ofetch'
import { useLocalStorage, watchDebounced } from '@vueuse/core'

const pdfSrc = ref<string | null>(null)

const valid = ref(false)
const formData = useLocalStorage('form-data', {})

watchDebounced(
  formData,
  async () => {
    if (!valid.value) {
      console.log('Form not valid')
      return
    }
    try {
      const blob = await ofetch('/api/pdf', {
        method: 'POST',
        body: formData.value,
        responseType: 'blob',
      })
      if (pdfSrc.value) {
        URL.revokeObjectURL(pdfSrc.value)
      }
      pdfSrc.value = URL.createObjectURL(blob)
    } catch (err) {
      console.log(err)
    }
  },
  { debounce: 500, maxWait: 5_000, deep: true, immediate: true },
)
</script>

<template>
  <v-container>
    <v-row>
      <v-col>
        <PermissionSlipForm v-model:valid="valid" v-model:data="formData"></PermissionSlipForm>
      </v-col>
      <v-col v-if="pdfSrc">
        <iframe :src="pdfSrc" width="100%" height="750px" />
        <v-btn
          color="primary"
          class="mt-4"
          :href="pdfSrc"
          download="permission-slip.pdf"
          target="_blank"
        >
          Download PDF
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
