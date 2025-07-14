<template>
  <div class="min-h-screen bg-gray-50">
    <nav class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <router-link to="/" class="text-xl font-bold text-green-600">Apaiser Café</router-link>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/" class="text-gray-700 hover:text-green-600">ホーム</router-link>
            <router-link to="/admin" class="text-gray-700 hover:text-green-600">管理画面</router-link>
          </div>
        </div>
      </div>
    </nav>

    <div class="max-w-4xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-gray-900 mb-8">お知らせ一覧</h1>
      
      <div v-if="loading" class="text-center py-8">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-green-600"></div>
        <p class="mt-2 text-gray-600">読み込み中...</p>
      </div>

      <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-md p-4 mb-6">
        <p class="text-red-800">{{ error }}</p>
      </div>

      <div v-else-if="announcements.length === 0" class="text-center py-12">
        <p class="text-gray-500 text-lg">現在お知らせはありません。</p>
      </div>

      <div v-else class="space-y-6">
        <div 
          v-for="announcement in announcements" 
          :key="announcement.id"
          class="bg-white rounded-lg shadow-md p-6 border border-gray-200"
        >
          <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-semibold text-gray-900">{{ announcement.title }}</h2>
            <span class="text-sm text-gray-500">{{ formatDate(announcement.created_at) }}</span>
          </div>
          <div class="text-gray-700 whitespace-pre-wrap">{{ announcement.content }}</div>
        </div>
      </div>

      <div class="mt-12 text-center">
        <router-link 
          to="/" 
          class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-green-600 hover:bg-green-700 transition-colors"
        >
          ホームに戻る
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Announcement {
  id: number
  title: string
  content: string
  created_at: string
}

const announcements = ref<Announcement[]>([])
const loading = ref(true)
const error = ref('')

const fetchAnnouncements = async () => {
  try {
    loading.value = true
    error.value = ''
    const response = await axios.get('http://localhost:8000/api/announcements')
    announcements.value = response.data
  } catch (err) {
    console.error('Failed to fetch announcements:', err)
    error.value = 'お知らせの取得に失敗しました。'
  } finally {
    loading.value = false
  }
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

onMounted(() => {
  fetchAnnouncements()
})
</script>
