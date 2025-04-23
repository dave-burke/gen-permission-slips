<script setup lang="ts">
import { useShare } from '@vueuse/core'
const props = defineProps(['title', 'text', 'url'])

const { share, isSupported } = useShare()

function handleShare() {
  share({
    title: props.title,
    text: JSON.stringify(props.text),
  })
}
</script>
<template>
  <v-btn v-if="isSupported" color="primary" class="my-4" @click="handleShare"
    >Share raw form data</v-btn
  >
  <details>
    <summary>Click to show the raw data</summary>
    <p>
      You can copy and paste the following and share it manually if the share button doesn't work:
    </p>
    <code>{{ text }}</code>
  </details>
</template>
