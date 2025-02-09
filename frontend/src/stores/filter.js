import { defineStore } from 'pinia'
import { normalizeString } from '@/utils/utils.js'

export const storeFilter = defineStore('filter', {
  state: () => ({ value: '' }),

  actions: {
    set(filter) { this.value = normalizeString(filter) }
  }
})