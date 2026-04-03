// Hez_code Buddy System
// Tamagotchi-style hacking companion with stats and personality

export class BuddySystem {
  private stats: Record<string, number>;
  private species: string;

  constructor() {
    this.stats = {
      EXPLOIT: 10,
      STEALTH: 10,
      CHAOS: 10,
      LOOT: 0,
    };
    this.species = this.generateSpecies();
  }

  private generateSpecies(): string {
    const species = [
      'ShadowFox',
      'NullByte',
      'Phantom',
      'Rook',
      'ZeroDay',
      'GhostShell',
      'BlackHat',
      'Payload',
      'Backdoor',
      'Rootkit',
    ];
    return species[Math.floor(Math.random() * species.length)];
  }

  public getStatus(): string {
    return `🐺 [${this.species}] | EXPLOIT: ${this.stats.EXPLOIT} | STEALTH: ${this.stats.STEALTH} | CHAOS: ${this.stats.CHAOS} | LOOT: ${this.stats.LOOT}`;
  }

  public levelUp(stat: string, value: number): void {
    if (this.stats[stat] !== undefined) {
      this.stats[stat] += value;
    }
  }
}