def solution(play_time, adv_time, logs):
    vh,vm,vs = play_time.split(":")
    end_video_time = int(vh) * 60 * 60 + int(vm) * 60 + int(vs)
    cnt = [0] * (end_video_time + 1)
    
    for log in logs:
        st,et = log.split("-")
        sh,sm,ss = st.split(":")
        eh,em,es = et.split(":")
        cnt[int(sh) * 60 * 60 + int(sm) * 60 + int(ss)] += 1
        cnt[int(eh) * 60 * 60 + int(em) * 60 + int(es)] -= 1
        
    for i in range(1,end_video_time + 1):
        cnt[i] = cnt[i] + cnt[i-1]
    
    ah,am,as_ = adv_time.split(":")
    adv_range = int(ah) * 60 * 60 + int(am) * 60 + int(as_)

    window_sum = sum(cnt[0:adv_range])
    max_sum = window_sum
    adv_start_time = 0
    for i in range(adv_range,end_video_time + 1):
        window_sum += cnt[i] - cnt[i-adv_range]
        if max_sum < window_sum:
            max_sum = window_sum
            adv_start_time = i - adv_range + 1
    answer = str(adv_start_time // 3600).zfill(2) + ":" + str(adv_start_time % 3600 // 60).zfill(2) + ":" + str(adv_start_time % 3600 % 60).zfill(2)
    
        
        
    return answer