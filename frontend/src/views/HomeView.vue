<script setup lang="ts">
import type { PermissionSlipData } from '@/components/permission-slip-form.types.ts'
import { useDisplay } from 'vuetify'
import { ref, computed, useTemplateRef } from 'vue'
import type { Ref } from 'vue'
import PermissionSlipForm from '@/components/PermissionSlipForm.vue'
import ShareContent from '@/components/ShareContent.vue'
import { ofetch } from 'ofetch'
import { useLocalStorage, watchDebounced } from '@vueuse/core'

const tab = ref(null)
const { smAndDown } = useDisplay()

const valid = ref(false)
const formData = useLocalStorage('form-data', {} as Ref<PermissionSlipData>)
const form = useTemplateRef<typeof PermissionSlipForm>('form')
const errors = computed(() => form.value?.errors ?? [])
const pdfSrc = ref<string | null>(null)

watchDebounced(
  formData,
  async () => {
    if (!valid.value) {
      console.log('Form not valid')
      pdfSrc.value = null
      return
    }
    try {
      const blob = await ofetch(`${import.meta.env.VITE_API_URL}/pdf`, {
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
  <v-card v-if="smAndDown">
    <v-tabs v-model="tab">
      <v-tab value="form">Data</v-tab>
      <v-tab value="pdf">Form</v-tab>
    </v-tabs>
    <v-card-text>
      <v-tabs-window v-model="tab">
        <v-tabs-window-item value="form">
          <PermissionSlipForm
            v-model:valid="valid"
            v-model:data="formData"
            ref="form"
          ></PermissionSlipForm>
          <ShareContent :title="`JSON data for ${formData.camp?.name}`" :text="formData" />
        </v-tabs-window-item>
        <v-tabs-window-item value="pdf">
          <template v-if="pdfSrc">
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
          </template>
          <template v-else>
            No PDF data. Is the form filled out fully and correctly?
            <ul>
              <li v-for="error in errors" :key="error.id">
                {{ error.errorMessages.join(", '") }}
              </li>
            </ul>
          </template>
        </v-tabs-window-item>
      </v-tabs-window>
    </v-card-text>
  </v-card>
  <v-container v-else>
    <v-row>
      <v-col>
        <PermissionSlipForm v-model:valid="valid" v-model:data="formData"></PermissionSlipForm>
        <ShareContent :title="`JSON data for ${formData.camp?.name}`" :text="formData" />
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
