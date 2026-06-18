import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='Malgun Gothic')

def plot_lhr_danger_zones():
    lhr_range = np.linspace(1.0, 4.0, 100)
    thresholds = np.select(
        [lhr_range >= 2.5, lhr_range >= 2.0, lhr_range < 2.0],
        [0, 10, 30], default=50
    )

    plt.figure(figsize=(10, 5))
    plt.fill_between(lhr_range, thresholds, color='skyblue', alpha=0.3, label='권장 섭취 범위')
    plt.plot(lhr_range, thresholds, color='navy', lw=2, linestyle='--')

    plt.axvspan(1.0, 2.0, color='green', alpha=0.1) # 정상
    plt.axvspan(2.0, 2.5, color='orange', alpha=0.1) # 주의
    plt.axvspan(2.5, 4.0, color='red', alpha=0.1) # 고위험

    plt.title('LHR 지수별 음식 콜레스테롤 허용 가이드', fontsize=20)
    plt.xlabel('LHR 지수 (LDL/HDL)')
    plt.ylabel('음식 콜레스테롤 허용치 (mg)')
    plt.text(1.3, 30, "정상: 균형식", fontsize=10, color='green')
    plt.text(2.1, 15, "위험: 저콜레스테롤", fontsize=10, color='orange')
    plt.text(3.0, 3, "고위험: ZERO(0mg) 필수", fontsize=10, color='red')
    plt.grid(True, alpha=0.2)
    plt.show()

plot_lhr_danger_zones()