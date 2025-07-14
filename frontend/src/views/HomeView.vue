<template>
  <div class="min-h-screen cafe-bg">
    <!-- Hero Section -->
    <section class="hero-section relative py-24 px-4">
      <div class="max-w-6xl mx-auto text-center">
        <h1 class="text-6xl font-bold coffee-brown mb-8 tracking-wide">Apaiser Café</h1>
        <p class="text-2xl forest-green mb-12 font-light leading-relaxed">森の中の穏やかなカフェで、心安らぐひとときを</p>
        <div class="flex justify-center space-x-6">
          <button 
            @click="scrollToReservation"
            class="wood-texture text-cream-text px-10 py-4 rounded-full hover:shadow-lg transition-all duration-300 font-semibold text-lg warm-shadow"
          >
            ご予約はこちら
          </button>
          <button 
            @click="scrollToMenu"
            class="bg-amber-700 text-cream-text px-10 py-4 rounded-full hover:bg-amber-800 transition-all duration-300 font-semibold text-lg warm-shadow"
          >
            メニューを見る
          </button>
        </div>
      </div>
      <div class="section-divider"></div>
    </section>

    <!-- About Section -->
    <section class="py-16 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="cafe-card rounded-lg p-8 mb-12">
          <h2 class="text-3xl font-bold forest-green mb-6 text-center">カフェについて</h2>
          <p class="text-gray-700 leading-relaxed mb-4">
            Apaiser Caféは、フランス語で「穏やかにする」という意味を持つ、森の中の静かなカフェです。
            自然に囲まれた落ち着いた空間で、厳選されたコーヒーと手作りのスイーツをお楽しみいただけます。
          </p>
          <p class="text-gray-700 leading-relaxed">
            忙しい日常から離れて、ゆったりとした時間をお過ごしください。
            読書やお仕事、友人との語らいなど、様々なシーンでご利用いただけます。
          </p>
        </div>
      </div>
    </section>

    <!-- Announcements Section -->
    <section class="py-20 px-4">
      <div class="max-w-4xl mx-auto">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold coffee-brown mb-4">お知らせ</h2>
          <div class="flex justify-center items-center">
            <span class="coffee-bean"></span>
            <span class="coffee-bean"></span>
            <span class="coffee-bean"></span>
          </div>
        </div>
        <div class="space-y-8">
          <div 
            v-for="announcement in announcements.slice(0, 3)" 
            :key="announcement.id"
            class="cafe-card organic-shape p-8 warm-shadow"
          >
            <h3 class="text-2xl font-semibold warm-brown mb-4">{{ announcement.title }}</h3>
            <p class="text-gray-700 mb-4 leading-relaxed text-lg">{{ announcement.content }}</p>
            <p class="text-sm coffee-brown font-medium">{{ formatDate(announcement.created_at) }}</p>
          </div>
        </div>
        <div class="text-center mt-12">
          <router-link 
            to="/announcements" 
            class="coffee-brown hover:warm-brown font-semibold text-lg transition-colors duration-300"
          >
            すべてのお知らせを見る →
          </router-link>
        </div>
      </div>
      <div class="section-divider"></div>
    </section>

    <!-- Menu Section -->
    <section id="menu" class="py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold coffee-brown mb-4">メニュー</h2>
          <div class="flex justify-center items-center">
            <span class="coffee-bean"></span>
            <span class="coffee-bean"></span>
            <span class="coffee-bean"></span>
          </div>
        </div>
        <div class="grid md:grid-cols-2 gap-12">
          <div class="cafe-card wood-texture p-8 warm-shadow">
            <h3 class="text-3xl font-semibold cream-text mb-6 text-center">ドリンク</h3>
            <div class="space-y-4">
              <div class="flex justify-between items-center py-2 border-b border-amber-200">
                <span class="cream-text text-lg">ブレンドコーヒー</span>
                <span class="font-bold cream-text text-xl">¥450</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-amber-200">
                <span class="cream-text text-lg">カフェラテ</span>
                <span class="font-bold cream-text text-xl">¥520</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-amber-200">
                <span class="cream-text text-lg">季節限定 桜ラテ</span>
                <span class="font-bold cream-text text-xl">¥580</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="cream-text text-lg">紅茶各種</span>
                <span class="font-bold cream-text text-xl">¥400</span>
              </div>
            </div>
          </div>
          <div class="cafe-card wood-texture p-8 warm-shadow">
            <h3 class="text-3xl font-semibold cream-text mb-6 text-center">フード・デザート</h3>
            <div class="space-y-4">
              <div class="flex justify-between items-center py-2 border-b border-amber-200">
                <span class="cream-text text-lg">手作りチーズケーキ</span>
                <span class="font-bold cream-text text-xl">¥480</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-amber-200">
                <span class="cream-text text-lg">抹茶チーズケーキ</span>
                <span class="font-bold cream-text text-xl">¥520</span>
              </div>
              <div class="flex justify-between items-center py-2 border-b border-amber-200">
                <span class="cream-text text-lg">本日のケーキ</span>
                <span class="font-bold cream-text text-xl">¥450</span>
              </div>
              <div class="flex justify-between items-center py-2">
                <span class="cream-text text-lg">サンドイッチセット</span>
                <span class="font-bold cream-text text-xl">¥780</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="section-divider"></div>
    </section>

    <!-- Business Hours & Access -->
    <section class="py-20 px-4">
      <div class="max-w-6xl mx-auto">
        <div class="grid md:grid-cols-2 gap-16">
          <!-- Business Hours -->
          <div class="cafe-card organic-shape p-8 warm-shadow">
            <h3 class="text-3xl font-semibold coffee-brown mb-6 text-center">営業時間</h3>
            <div class="space-y-4">
              <div class="flex justify-between items-center py-3 border-b border-amber-200">
                <span class="text-lg forest-green">平日</span>
                <span class="font-semibold text-lg coffee-brown">9:00 - 20:00</span>
              </div>
              <div class="flex justify-between items-center py-3 border-b border-amber-200">
                <span class="text-lg forest-green">土日祝</span>
                <span class="font-semibold text-lg coffee-brown">9:00 - 21:00</span>
              </div>
              <div class="mt-6 text-center">
                <p class="text-warm-brown font-medium">定休日: 毎週火曜日</p>
                <p class="text-sm text-gray-600 mt-2">※祝日の場合は営業いたします</p>
              </div>
            </div>
          </div>

          <!-- Contact Info -->
          <div class="cafe-card organic-shape p-8 warm-shadow">
            <h3 class="text-3xl font-semibold coffee-brown mb-6 text-center">アクセス・お問い合わせ</h3>
            <div class="space-y-4">
              <p class="text-lg"><strong class="coffee-brown">住所:</strong> <span class="forest-green">栃木県宇都宮市塙田1-1-20</span></p>
              <p class="text-lg"><strong class="coffee-brown">電話:</strong> <span class="forest-green">028-623-1234</span></p>
              <p class="text-lg"><strong class="coffee-brown">メール:</strong> <span class="forest-green">info@apaiser-cafe.com</span></p>
              <div class="mt-6 text-center">
                <p class="text-warm-brown font-medium">栃木県庁より徒歩5分</p>
                <p class="text-warm-brown font-medium">駐車場完備（20台）</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="section-divider"></div>
    </section>

    <!-- Google Maps -->
    <section class="py-16 px-4">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold forest-green mb-8 text-center">アクセスマップ</h2>
        <div class="cafe-card rounded-lg p-4">
          <div class="w-full h-96 rounded-lg overflow-hidden">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3222.8234567890123!2d139.8836!3d36.5658!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x601f676b1234567%3A0x1234567890abcdef!2z5qCg5pyo55yM5bqB!5e0!3m2!1sja!2sjp!4v1234567890123!5m2!1sja!2sjp"
              width="100%"
              height="100%"
              style="border:0;"
              allowfullscreen=""
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
            ></iframe>
          </div>
        </div>
      </div>
    </section>

    <!-- Reservation Section -->
    <section id="reservation" class="py-20 px-4">
      <div class="max-w-3xl mx-auto">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold coffee-brown mb-4">ご予約</h2>
          <div class="flex justify-center items-center">
            <span class="coffee-bean"></span>
            <span class="coffee-bean"></span>
            <span class="coffee-bean"></span>
          </div>
        </div>
        <div class="cafe-card organic-shape p-10 warm-shadow">
          <form @submit.prevent="submitReservation" class="space-y-8">
            <div>
              <label class="block text-lg font-semibold coffee-brown mb-3">お名前 *</label>
              <input
                v-model="reservation.name"
                type="text"
                required
                class="w-full px-4 py-3 border-2 border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-lg"
              />
            </div>
            
            <div>
              <label class="block text-lg font-semibold coffee-brown mb-3">電話番号 *</label>
              <input
                v-model="reservation.phone"
                type="tel"
                required
                class="w-full px-4 py-3 border-2 border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-lg"
              />
            </div>
            
            <div>
              <label class="block text-lg font-semibold coffee-brown mb-3">メールアドレス *</label>
              <input
                v-model="reservation.email"
                type="email"
                required
                class="w-full px-4 py-3 border-2 border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-lg"
              />
            </div>
            
            <div>
              <label class="block text-lg font-semibold coffee-brown mb-3">人数 *</label>
              <select
                v-model="reservation.party_size"
                required
                class="w-full px-4 py-3 border-2 border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-lg"
              >
                <option value="">選択してください</option>
                <option v-for="i in 8" :key="i" :value="i">{{ i }}名</option>
              </select>
            </div>
            
            <div>
              <label class="block text-lg font-semibold coffee-brown mb-3">予約日時 *</label>
              <input
                v-model="reservation.reservation_date"
                type="datetime-local"
                required
                class="w-full px-4 py-3 border-2 border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-lg"
              />
            </div>
            
            <div>
              <label class="block text-lg font-semibold coffee-brown mb-3">備考</label>
              <textarea
                v-model="reservation.notes"
                rows="4"
                class="w-full px-4 py-3 border-2 border-amber-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500 text-lg"
                placeholder="アレルギーやご要望などがございましたらお書きください"
              ></textarea>
            </div>
            
            <button
              type="submit"
              :disabled="isSubmitting"
              class="w-full wood-texture cream-text py-4 px-6 rounded-lg hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-amber-500 disabled:opacity-50 text-xl font-semibold warm-shadow transition-all duration-300"
            >
              {{ isSubmitting ? '送信中...' : '予約を送信' }}
            </button>
          </form>
          
          <div v-if="reservationMessage" class="mt-6 p-4 rounded-lg" :class="reservationMessageClass">
            {{ reservationMessage }}
          </div>
        </div>
      </div>
    </section>
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
  updated_at: string
}

interface ReservationForm {
  name: string
  phone: string
  email: string
  party_size: number | string
  reservation_date: string
  notes: string
}

const announcements = ref<Announcement[]>([])
const reservation = ref<ReservationForm>({
  name: '',
  phone: '',
  email: '',
  party_size: '',
  reservation_date: '',
  notes: ''
})

const isSubmitting = ref(false)
const reservationMessage = ref('')
const reservationMessageClass = ref('')

const API_BASE_URL = 'http://localhost:8000'

const fetchAnnouncements = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/announcements`)
    announcements.value = response.data
  } catch (error) {
    console.error('Failed to fetch announcements:', error)
  }
}

const submitReservation = async () => {
  isSubmitting.value = true
  reservationMessage.value = ''
  
  try {
    const reservationData = {
      ...reservation.value,
      party_size: Number(reservation.value.party_size)
    }
    
    const response = await axios.post(`${API_BASE_URL}/api/reservations`, reservationData)
    
    reservationMessage.value = 'ご予約を承りました。確認メールをお送りいたします。'
    reservationMessageClass.value = 'bg-green-100 text-green-800 border border-green-200'
    
    // Reset form
    reservation.value = {
      name: '',
      phone: '',
      email: '',
      party_size: '',
      reservation_date: '',
      notes: ''
    }
  } catch (error) {
    console.error('Failed to submit reservation:', error)
    reservationMessage.value = 'ご予約の送信に失敗しました。もう一度お試しください。'
    reservationMessageClass.value = 'bg-red-100 text-red-800 border border-red-200'
  } finally {
    isSubmitting.value = false
  }
}

const formatDate = (dateString: string) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const scrollToReservation = () => {
  document.getElementById('reservation')?.scrollIntoView({ behavior: 'smooth' })
}

const scrollToMenu = () => {
  document.getElementById('menu')?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => {
  fetchAnnouncements()
})
</script>
